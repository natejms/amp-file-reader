# amp-file-reader
An Ampersand plugin allowing you to read files as translations

## Basic usage
Assuming you have a file titled "content.txt" in your translation's directory,
you can write the following to read the file into your JSON translation.

```
{
  "file": "file:content.txt"
}
```

Upon rendering, `file:content.txt` will be replaced with the contents of the
file.

## Installation
You can add amp-file-reader to your project with the following:

```
$ amp plugin add https://github.com/natejms/amp-file-reader.git
```
