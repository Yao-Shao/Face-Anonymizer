# ROSBAG-Anonymizer

This is a tool to anonymize sensitive information(face & license plate) from real world pictures. I also implement the ROSBAG IO code which can extract pictures and write them back to ROSBAG files.

> Author: **Yao Shao**
>
> Contact: **yshao998@gmail.com**

## Usage

1. Extract

   use `bag_process.py` in the [bag_extract]( https://github.com/Yao-Shao/ROSBAG-Anonymizer/tree/master/bag_extract ) folder to extract pictures for anonymization.

2. Anonymization

   The anonymization algorithm is developed by [understand.ai]( https://understand.ai/ ).

   - clone the [repo]( https://github.com/understand-ai/anonymizer), build and test it.

   - use the `auto.py` in the [blur_gpu]( https://github.com/Yao-Shao/ROSBAG-Anonymizer/tree/master/blur_gpu) folder to automated blur pictures in multiple folders.

   - remember to install all dependencies needed by

     ```shell
     pip install -r requiremnts.txt
     ```

3. Write back

   use `write_bag.py` in the [write_bag]( https://github.com/Yao-Shao/ROSBAG-Anonymizer/tree/master/write_bag ) folder to write the anonymized data back to the original bag file.

## References

1. [Anonymizer]( https://github.com/understand-ai/anonymizer)