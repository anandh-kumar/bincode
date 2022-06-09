from PIL import Image
import time
size_of_qrCode = 1000
size_of_one_pixel = 50


def image_to_bin(bincode: Image):
    counter = 1
    pos = 0
    coordY = 1
    pixel_values = list(bincode.getdata())
    binary = ""
    for byte in range(size_of_qrCode):
        # Checks for black box
        if pixel_values[pos] == 0:
            binary += "0"
        # Checks for white box
        else:
            binary += "1"
        # print(size_of_qrCode * size_of_qrCode - size_of_one_pixel * size_of_qrCode + (size_of_qrCode / size_of_one_pixel - 1) * size_of_one_pixel)
        if pos == size_of_qrCode * size_of_qrCode - size_of_one_pixel * size_of_qrCode + (size_of_qrCode / size_of_one_pixel - 1) * size_of_one_pixel:
            break

        # print(pixel_values[pos], pos, binary)
        # Checks for end for X axis
        if counter == size_of_qrCode/size_of_one_pixel:
            pos = size_of_qrCode * size_of_one_pixel * coordY
            counter = 0
            coordY += 1
        else:
            pos += size_of_one_pixel

        # time.sleep(1)
        counter += 1

    return binary


def format_binary(text: str):
    # Formats the binary produced
    pos = 0
    binary = ""
    for bit in text:
        if pos == 7:
            binary += " "
            pos = 0
        binary += bit
        pos += 1
    return binary


def bin_to_char(binary: str):
    # Converts binary to char
    text = ""
    for byte in binary.split():
        print(byte, chr(int(byte, 2)))
        if(byte == "1111111"):
            break
        text = text + chr(int(byte, 2))

    return text


def encoder():
    text = input("Enter the text: ")
    # Basic setup
    base_image = Image.new("1", (size_of_qrCode, size_of_qrCode), 1)
    black_box = Image.new("1", (size_of_one_pixel, size_of_one_pixel))
    coor_X = 0
    coor_Y = 0

    # Iterates through each character
    for char in text:
        # Converts them to bin
        byte = str(bin(ord(char))[2:])

        # Iterates through each bit
        for bit in byte:

            # Checks if reached end of image (X)
            if coor_X == size_of_qrCode:
                coor_X = 0
                coor_Y += size_of_one_pixel

            # Gives black color for 0
            if bit == '0':
                base_image.paste(black_box, (coor_X, coor_Y))
            coor_X += size_of_one_pixel
    base_image.save('bincode.png')
    # print()


def decoder():
    binary = image_to_bin(bincode=Image.open('bincode.png'))
    binary = format_binary(binary)
    text = bin_to_char(binary)
    print(text)


encoder()
decoder()
# text = format_binary("1101000110010111011010110110011011111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111")
# text = bin_to_char("1101000 1100101 1101101 0110110 0110111")
# print(text)
