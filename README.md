# SeedSigner Translations

## Transifex CLI
You can pull the latest translations directly from Transifex. 

* Install the [Transifex CLI](https://developers.transifex.com/docs/cli).
* Create a user account on Transifex.
* [Create an API key](https://help.transifex.com/en/articles/6248858-generating-an-api-token)
for your Transifex user.

Since our Transifex project is public, all of our translations should be accessible with
no special permissions required for your Transifex user.

From the `seedsigner/src/seedsigner/resources/seedsigner-translations` dir run:

```bash
# --all, -a  Whether to download all files (default: false)
tx pull --all
```

The `.tx/config` is set to `minimum-perc = 15` (this means that the CLI will skip any
language whose translation completion falls below this minimum percentage). You can
manually override this by adding, for example, `--minimum-perc 25` to require at least 25%
translation completion.

Then from the SeedSigner project root, compile the catalogs to process the *.po files into
*.mo:

```bash
python setup.py compile_catalog
```