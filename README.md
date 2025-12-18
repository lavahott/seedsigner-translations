# SeedSigner Translations

## Transifex CLI
You can pull the latest translations directly from Transifex (requires a user with privleges to our Transifex project).

Install the [Transifex CLI](https://developers.transifex.com/docs/cli).

[Create an API key](https://help.transifex.com/en/articles/6248858-generating-an-api-token) for your Transifex user.

From the `seedsigner/src/seedsigner/resources/seedsigner-translations` dir run:

```bash
# --all, -a             Whether to download all files (default: false)
# --minimum-perc value  Specify the minimum acceptable percentage of a translation mode in order to download it. (default: -1)
tx pull --all --minimum-perc 15
```

Then from the SeedSigner project root, compile the catalogs to process the *.po files into *.mo:
```bash
python setup.py compile_catalog
```