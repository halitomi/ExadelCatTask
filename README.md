Task:
* Write code that generates n random unique square fragments from the image.
* The fragments are supposed to come from the inside or outside of the bounding box, depending on the value of the variable inside.
* We assume that the size is smaller than the bounding box - the generated fragments should be entirely contained within it (when inside = True).
* Save the cut-outs as jpg files in a folder created in your script called output_folder.
* Before saving, delete the contents of this folder and create this folder again.

## How to run

1. Install the required packages:

   ```bash
   pip install pillow matplotlib
   ```
   or
   
   ```bash
    pip install -r requirements.txt
   ```

2. Run the script:

  ``` bash
 python task.py
  ```


The generated fragments will appear in the output folder.

Files included:
task.py
cat.jpg
requirements.txt
