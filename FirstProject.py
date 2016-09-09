from PIL import Image

def median(Dlist = []):
    sortedList = sorted(Dlist)
    if (len(Dlist)%2!=0):
        middleIndex = ((len(Dlist)+1)/2)-1
    else:
        middleIndex = (len(Dlist)/2)
    return sortedList[int(middleIndex)]

def main():
    #Opening Images
    #//////////////////////////////
    total_images = 0
    image_list = [] #List for holding image objects
    image_data = [] #List that holds lists of RGB data for each pixel as tuples (confusing)
    image_size = 0
    total_pixels = 0
    finalimage_data = [] #List of RGB tuples representing pixel data for final image
    finalimage = Image
    total_images = input("Enter amount of images: ")
    print("Make sure all images are in the same directory as this program")
    print("Images should be inputed as name followed by format: name.png")
    file_name = ""
    #File processing
    #//////////////////////////////
    for i in range (int(total_images)):
        image_list.append(Image)
        file_name = input("Enter a filename: ") #Reading image names
        image_list[i] = Image.open(file_name)#Opening images
        #print(image_list[i].size)
        image_data.append(list(image_list[i].getdata())) #Appending each image's data into image data list
    image_size = image_list[0].size
    total_pixels =  image_size[0]*image_size[1]
    finalimage = Image.new("RGB", image_size , "black")

    #Image data processing
    #//////////////////////////////
    redarray = [] #Lists to temporarily hold the RGB data of a single pixel from the same location of all images
    greenarray = [] 
    bluearray = []
    print ("Image size: ", image_size, "Total pixels: ", image_size[0]*image_size[1])
    print ("Applying median filter...")
    for k in range (total_pixels):
        for i in range (int(total_images)):
            redarray.append(image_data[i][k][0]) #Reading pixel data from a single location of all images into RGB lists
            greenarray.append(image_data[i][k][1])
            bluearray.append(image_data[i][k][2])
        redmedian = median(redarray) #Calculating medians of RGB lists
        greenmedian = median(greenarray)
        bluemedian = median(bluearray)
        finalimage_data.append ((redmedian, greenmedian, bluemedian)) #Appending RGB medians as tuples to list holding final image data
        redarray.clear()#Clearing lists for next pixel location to be processed
        greenarray.clear()
        bluearray.clear()
        #print("Current pixel: ", k, "R med: ", redmedian, "G med: ", greenmedian, "B med: ", bluemedian)
        #print("Tuple for this pixel: ", finalimage_data[k])
    finalimage.putdata(finalimage_data)
    finalimage.save("Final.png")
    print("DONE!")

if __name__ == "__main__":
    main()

    



