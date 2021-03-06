# External DSL for video montage using Python and moviepy library

## ImageMagick Linux SETUP/FIX:

```bash
$ whereis magick \
magick: /usr/bin/magick /usr/share/man/man1/magick.1.gz
```

In Actions.py:
```python
if sys.platform != 'linux':
   change_settings({"IMAGEMAGICK_BINARY": r"C:\\Program Files\\ImageMagick-7.0.11-Q16\\magick.exe"})
else:
   change_settings({"IMAGEMAGICK_BINARY": r"/usr/bin/magick"}) #here
```

Modify fichier:
```/etc/ImageMagick-7/policy.xml```

comment following line:

```xml
<policy domain="path" rights="none" pattern="@*" />
```
in
```xml
<!-- <policy domain="path" rights="none" pattern="@*" /> -->
```
