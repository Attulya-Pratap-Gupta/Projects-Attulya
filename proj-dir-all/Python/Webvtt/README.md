# VTT to DOCX Converter

This Python script converts VTT (WebVTT) subtitle files to DOCX (Microsoft Word) format. It reads a VTT file, extracts speaker names and their corresponding speech content, and organizes them into a structured DOCX document.

## Usage

1. **Requirements:**

   - Python 3.x
   - `webvtt` and `python-docx` libraries (you can install them using `pip`)

   ```bash
   pip install webvtt-py python-docx
   ```

2. **Clone the Repository:**

   Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   ```

3. **Run the Script:**

   Replace `'Team23_220808.vtt'` with the path to your VTT file in the script (`convert_vtt_to_docx.py`).

   ```python
   for caption in webvtt.read('your_vtt_file.vtt'):
   ```

4. **Execute the Script:**

   Run the Python script to generate the DOCX file:

   ```bash
   python convert_vtt_to_docx.py
   ```

5. **Output:**

   The DOCX file will be generated as `test1.docx` in the same directory as the script. You can customize the output filename by modifying the following line in the script:

   ```python
   word_document.save('your_output_filename.docx')
   ```

## Example

For an input VTT file like this:

```vtt
00:00:00.000 --> 00:00:05.000
Speaker 1: Hello, world!

00:00:05.100 --> 00:00:10.000
Speaker 2: Hi there.

00:00:10.500 --> 00:00:15.000
Speaker 1: How are you?
```

The script will generate a DOCX file with the following structure:

### Audio file

Team23_220808

### Transcript

- 00:00:00 Speaker 0
  - Hello, world!
- 00:00:05 Speaker 1
  - Hi there.
- 00:00:10 Speaker 0
  - How are you?

## Acknowledgments

- Thanks to the creators of the `webvtt` and `python-docx` libraries for making this conversion process easier.
- If you have any questions or feedback, please feel free to open an issue or contact us.

