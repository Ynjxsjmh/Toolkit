from PIL import Image
import DHash

if __name__ == "__main__":
    image1 = Image.open(r"E:\2我的收藏夹\小米画报\Screenshot_2018-06-02-17-18-23-126_lockscreen.png")
    image2 = Image.open(r"E:\2我的收藏夹\小米画报\Screenshot_2018-06-02-17-18-28-413_lockscreen.png")
    hamming_distance = DHash.hamming_distance(image1,image2)
    print(hamming_distance)
