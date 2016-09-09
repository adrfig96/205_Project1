from PIL import Image

def median(Dlist = []):
    sortedList = sorted(Dlist)
    middleIndex = ((len(Dlist)+1)/2)-1
    return sortedList[int(middleIndex)]

def main():
    #Opening Images
    #//////////////////////////////
    image_list = [] 
    image_data = []
    image_size = 0
    total_pixels = 0
    finalimage_data = []
    finalimage = Image
    for i in range (9):
        image_list.append(Image)
        image_list[i] = Image.open(str(i+1)+".png")
        #print(image_list[i].size)
        image_data.append(list(image_list[i].getdata()))
    image_size = image_list[0].size
    total_pixels =  image_size[0]*image_size[1]
    finalimage = Image.new("RGB", image_size , "red")

    #Processing
    #//////////////////////////////
    redarray = []
    greenarray = []
    bluearray = []
    print ("Image size: ", image_size, "Total pixels: ", image_size[0]*image_size[1])
    print ("Applying median filter...")
    for k in range (total_pixels):
        for i in range (9):
            redarray.append(image_data[i][k][0])
            greenarray.append(image_data[i][k][1])
            bluearray.append(image_data[i][k][2])
        redmedian = median(redarray)
        greenmedian = median(greenarray)
        bluemedian = median(bluearray)
        finalimage_data.append ((redmedian, greenmedian, bluemedian))
        redarray.clear()
        greenarray.clear()
        bluearray.clear()
        #print("Current pixel: ", k, "R med: ", redmedian, "G med: ", greenmedian, "B med: ", bluemedian)
        #print("Tuple for this pixel: ", finalimage_data[k])
    finalimage.putdata(finalimage_data)
    finalimage.save("Final.png")
    print("DONE!")
    #image_data is a list of list of tuples
    #Where the first index is which image, the second is which pixel, and the tuple is the RGB values
    #For example, [0][3][1] is the first image, 4th pixel in the first row, and the green band
    #FIND MEDIAN OF EACH BAND THEN PUT THEM SEPARATELY INTO NEW PICTURE

if __name__ == "__main__":
    main()

    



