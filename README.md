# ROSBAG-Anonymizer

This is a tool to anonymize sensitive information(faces & license plates) from real world pictures. I also implement the ROSBAG IO code which can extract pictures, blur them and then write back to the same ROSBAG files.

> Author: **Yao Shao**
>
> Contact: **yshao998@gmail.com**

## Usage

1. Extraction

   Extract pictures from the original ROSBAG files.

2. Anonymization

   The anonymization algorithm is developed by [understand.ai]( https://understand.ai/ ).

   - clone the [repo]( https://github.com/understand-ai/anonymizer), build and test it.
   
   - install all dependencies needed.

     ```shell
     pip install -r requiremnts.txt
     ```

   - you may find `auto.py` helpful if you want to blur pictures in multiple folders.


3. Writing back

   use `write_bag.py` to write the anonymized data back to the original bag file.

## References

1. [Anonymizer]( https://github.com/understand-ai/anonymizer)
