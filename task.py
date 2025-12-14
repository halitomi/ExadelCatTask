
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import os
import shutil
import random
from PIL import Image


def generate_fragments(image, bounding_box, n, size, inside, output_folder):
    """
    Generates n random unique square fragments from the given cat picture.
    """

    # Output folder setup. Make sure the output folder is clean
    if os.path.exists(output_folder):
        shutil.rmtree(output_folder)
    os.makedirs(output_folder, exist_ok=True)

    width, height = image.size


    # Normalize bounding box
    (bx1, by1), (bx2, by2) = bounding_box

    x_min = min(bx1, bx2)
    x_max = max(bx1, bx2)
    y_min = min(by1, by2)
    y_max = max(by1, by2)

    if inside:
        if x_max - x_min < size or y_max - y_min < size:
            raise ValueError("Bounding box is smaller than fragment size.")
        
    fragments = set()  # store (x, y) positions without duplicates

    max_attempts = n * 20 
    attempts = 0

    while len(fragments) < n and attempts < max_attempts:
        attempts += 1

        if inside:
            # sample directly inside the bounding box
            x = random.randint(x_min, x_max - size)
            y = random.randint(y_min, y_max - size)
        else:
            # sample anywhere in the image
            x = random.randint(0, width - size)
            y = random.randint(0, height - size)


        # check if the square is inside bounding box
        inside_bb = (
            x >= x_min and x + size <= x_max and
            y >= y_min and y + size <= y_max
        )

        #outside of bounding box
        outside_bb = (
            x + size <= x_min or
            x >= x_max or
            y + size <= y_min or
            y >= y_max
        )

        # Keep based on inside/outside requirement
        if inside and not inside_bb:
            continue
        if not inside and not outside_bb:
            continue

        
    
        fragments.add((x, y))

    if len(fragments) < n:
        raise ValueError(
            f"Could not generate {n} fragments with given constraints."
        )


    # Fragment saving
    for idx, (x, y) in enumerate(fragments):
        crop = image.crop((x, y, x + size, y + size))
        crop = crop.convert("RGB")
        crop.save(os.path.join(output_folder, f"fragment_{idx}.jpg"), "JPEG")

    print(f"Generated {len(fragments)} fragments in the '{output_folder}'")


def main():
    image = Image.open('cat.jpg')

    bounding_box = ((200, 730), (630, 120))
    n = 100
    size = 30
    inside = True
    output_folder = 'output'

    # code for viewing the bounding box
    fig, ax = plt.subplots()
    ax.imshow(image)
    width = bounding_box[1][0] - bounding_box[0][0]
    height = bounding_box[1][1] - bounding_box[0][1]
    rect = Rectangle(bounding_box[0], width, height, linewidth=1, edgecolor='r', facecolor='none')
    ax.add_patch(rect)
    plt.show()

    generate_fragments(image, bounding_box, n, size, inside, output_folder)


if __name__ == "__main__":
    main()


