import os
import cv2
def transform(input_path, output_path):
    for root, dirs, files in os.walk(input_path):
        for name in files:
            file = os.path.join(root, name)
            print('transform' + name)
            a = name[-4:]
            if name[-4:] == '.JPG':
                im = cv2.imread(file)
                if output_path:
                    cv2.imwrite(os.path.join(output_path, name.replace('JPG', 'png')), im)
                else:
                    cv2.imwrite(file.replace('JPG', 'png'), im)


if __name__ == '__main__':
    input_path = r"Z:\sys\data\dior\images\test"

    output_path = r"Z:\sys\data\dior\images_1024\test"
    if not os.path.exists(input_path):
        print("文件夹不存在!")
    else:
        print("Start to transform!")
        transform(input_path, output_path)
        print("Transform end!")

