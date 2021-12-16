import os 

def main():
    i = 0
    path = os.getcwd() + "/test/"
    for filename in os.listdir(path):
        src = path + filename
        dest = path +  "rename" + str(i) + ".md"
        os.rename(src, dest)
        i += 1
    print("Rename files successfully...")

if __name__ == '__main__':
    main()

