from PIL import Image
import wikipedia


def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,(img_height - crop_height) // 2,(img_width + crop_width) // 2,(img_height + crop_height) // 2))

def crop_max_square(pil_img):
    return crop_center(pil_img, min(pil_img.size), min(pil_img.size))

def Crop(upload):
    im = Image.open(upload)
    im_new = crop_max_square(im)
    im_new.save(upload, quality=100)


def wiki(filename):
    if(filename=="Aamir_Khan"):
        return("Mohammed Aamir Hussain Khan, born 14 March 1965 is an Indian actor, film director, producer, and television talk show host who works in Hindi films. Through his career spanning over 30 years, Khan has established himself as one of the most popular and influential actors of Indian cinema. He has a large global following, especially in India and China, and has been described by Newsweek as \"the biggest movie star\" in the world. Khan is the recipient of numerous awards, including nine Filmfare Awards, four National Film Awards, and an AACTA Award.")
    elif(filename=="Akshaye_Khanna"):
        return("Akshaye Vinod Khanna (born 28 March 1975) is an Indian actor who appears in Hindi films. He is the son of late Indian actor Vinod Khanna. He has also won numerous awards in his career including two Filmfare Awards, three Screen Awards and two IIFA Awards in varied acting categories. After studying in Kishore Namit Kapoor Acting Institute in Mumbai, he made his acting debut in 1997 with the film Himalay Putra.")
    else:
        return(wikipedia.summary(filename, sentences=4))


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def heading(filename):
    title=[]
    title2=""
    title=(filename.split('/')[1]).split('_')
    for titles in title:
        title2+=titles+" "
    return title2