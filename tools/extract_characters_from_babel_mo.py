# extract_characters_from_babel_mo.py

"""
This is a utility for build / dev purposes. 
"""

if __name__ == "__main__":
  import sys
  from babel.messages import mofile

  include_chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-=|?><,.;:[]{}"

  # read first argument to get path of babel mo file
  mo_fullfilename = sys.argv[1]
  with open(mo_fullfilename, "rb") as f:
    catalog = mofile.read_mo(f)

  all_chars = []
  for msg in catalog:
    if msg.string:
      if isinstance(msg.string, list):
        # pural message
        all_chars.extend(msg.string)
      else:
        # singular message
        all_chars.append(msg.string)


  # get a unique list of chars from all translation messages and included_chars string
  chars = sorted(set("".join(all_chars) + include_chars))

  # convert set to string
  chars_string = "".join(chars)

  # remove newlines
  chars_string = chars_string.replace("\n", "").replace("\r", "")

  print(chars_string)
