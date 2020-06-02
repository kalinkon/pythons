from zipfile import ZipFile
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import pytesseract
import cv2 as cv
import numpy as np
import math
import PIL
# loading the face detection classifier
face_cascade = cv.CascadeClassifier('readonly/haarcascade_frontalface_default.xml')
font_file ="readonly/fanwood-webfont.ttf"
# the rest is up to you!

def read_zip_files(file_path):
    images = []
    with ZipFile(file_path) as archive:
        for entry in archive.infolist():
            with archive.open(entry) as file:
                img = Image.open(file)
                # img.show()
                print(img.size, img.mode, len(img.getdata()))
                images.append({"image": img, "name": entry.filename, "text": ""})
    return images


def get_texts_from_images(images, keyword):
    result_list = []
    for image_object in images:
        image = image_object["image"].convert("1")
        print("working")
        text = pytesseract.image_to_string(image)
        image_object["text"] = text
        if keyword in text:
            result_list.append(image_object)

    return result_list

def find_faces(images):
    for image_obj in images:
        image = image_obj["image"].convert("1")
        image = image_obj["image"].filter(ImageFilter.SHARPEN)
        cv_image = pil_to_cv(image)
        cv_image = cv.cvtColor(cv_image, cv.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(cv_image, scaleFactor=2.0, minSize=(25, 25),flags = cv.CASCADE_SCALE_IMAGE)
        image_obj["faces"] = faces
    return images


def pil_to_cv(pil_image):
    # Convert RGB to BGR
    return np.array(pil_image)[:, :, ::-1].copy()


def make_thumbnail(image):
    size = (100, 100)
    image.thumbnail(size, Image.ANTIALIAS)
    background = Image.new('RGBA', size, (255, 255, 255, 0))
    # background.paste(
    #     image, (int((size[0] - image.size[0]) / 2), int((size[1] - image.size[1]) / 2))
    # )
    background.paste(
        image, (0,0)
    )
    # background.save("junk/output.png")
    return background


def create_image_sheet(image_obj):
    image = image_obj["image"]
    faces = image_obj["faces"]

    if len(faces) != 0:
        number_of_row = math.ceil((len(faces)) / 5)
        collage_sheet = Image.new(image.mode, (500,  100 * number_of_row))
        # collage_sheet.show()
        count = 0
        m = 0
        n = 0
        for x,y,w,h in faces:
            count += 1
            # face = image.crop((x,y, x+w, y+h))
            extra = 30
            # face = image.crop((x+extra,y+extra, x+w+extra, y+h+extra))
            face = image.crop((x,y, x+w, y+h))
            # face = face.thumbnail([100, 100],PIL.Image.ANTIALIAS)
            print(m, n)
            thumb = make_thumbnail(face)
            collage_sheet.paste(thumb, (m, n))
            # face.save("junk/{}.jpg".format(str(count)))
            m += 100
            if m > 400:
                m=0
                n+=100
    else:
        text = "But there were no faces in the file!"
        text_height = 35
        collage_sheet = Image.new('RGB', (500, text_height), color=(255, 255, 255))
        draw = ImageDraw.Draw(collage_sheet)
        draw.text((0, 5), text, (0, 0, 0), font=ImageFont.truetype(font_file, text_height // 2))

    return collage_sheet

    # collage_sheet.save("junk/col.jpg")
        # face.show()

def add_text(image_obj, image_sheet):
    text = "Results found in file {}".format(str(image_obj["name"]))
    text_height = 35
    text_img = Image.new('RGB', (image_sheet.width, text_height), color=(255, 255, 255))
    draw = ImageDraw.Draw(text_img)
    draw.text((0, 5), text, (0, 0, 0), font=ImageFont.truetype(font_file, text_height // 2))
    text_sheet = PIL.Image.new(image_sheet.mode, (image_sheet.width , image_sheet.height + text_height))
    text_sheet.paste(text_img, (0, 0 ))
    text_sheet.paste(image_sheet, (0, text_height) )
    return text_sheet

def join_all_images(images):
    # final_sheet.save("junk/col.jpg")
    final_images = []
    for image in images:
        image_sheet = create_image_sheet(image)
        final_sheet = add_text(image, image_sheet)
        final_images.append(final_sheet)

    width, height = get_image_height_width(final_images)
    collage_sheet = Image.new(final_images[0].mode, (width, height))
    # collage_sheet.save("junk/tests.jpg")
    n = 0
    for image in final_images:
        # image.save("junk/tests1.jpg")
        collage_sheet.paste(image, (0, n))
        # collage_sheet.save("junk/tests.jpg")
        n += image.height

    # collage_sheet.save("junk/final.jpg")
    return collage_sheet


def get_image_height_width(images):
    width, height = [images[0].width, 0]
    for im in images:
        height += im.height
        print(width, height)
    return width, height


# if __name__ == "__main__":
    # keyword = "Christopher"
keyword = input("Please enter the keyword you want to search for:")
images = read_zip_files("readonly/small_img.zip")
images_with_texts = get_texts_from_images(images, keyword)
images_with_faces = find_faces(images_with_texts)
final_sheet = join_all_images(images_with_faces)
# image_sheet = create_image_sheet(images_with_faces[0])
# final_sheet = add_text(images_with_faces[0], image_sheet)
print("worked")

display(final_sheet)
