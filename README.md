# Submitting SeedSigner translation changes

Create an account on github.com if you haven't already.

---

### Finish translation changes, download .po file
* Update and review translations in Transifex.
* Navigate to this screen in Transifex and click "Download for use":

<p align="center">
  <img width="500" src="https://gist.github.com/user-attachments/assets/0a332a7e-2f75-4a44-a3bf-4c8126139588" />
</p>

* IMPORTANT: Rename the downloaded file to: `messages.po`

---

### Fork the `seedsigner-translations` repo
(skip this step if you've already forked it)

In order to submit a change, you'll need your own copy of the `seedsigner-translations` repo. Make sure you're signed in to your github account and then:
* Go to the [translations repo](https://github.com/SeedSigner/seedsigner-translations)
* Click "fork" at the top right.

<img width="600" alt="Screenshot 2025-01-13 at 3 43 58 PM" src="https://gist.github.com/user-attachments/assets/b817df7e-2850-48cf-bc83-9354ac66c0d1" /><br/>

Leave all the defaults as they are and proceed with creating the fork.

---

### If use the github.com website to edit your own fork of `seedsigner_translations`
Start by selecting the branch you want to work in

* select the l10n folder
* upper left corner, next to the "branch" select menu, click the icon that expands the file tree,
* click "+" to start a new file in the right-side frame editor,
* at the very top where you name the file, as you add "pl/" you'll see a new folder grow in l10n.  As you enter "LC_MESSAGES/" you'll see that become a folder too, then you can finish by naming your file "messages.po"

Trouble shooting: remove the existing file named "pl".  l10n already has it in your repo, so it's complaining that a file is taking the place of where you want to put a folder.  Then try same again after file "pl" is no longer there.

---

### Upload your changes to your fork
Your browser url should now be: github.com/<your_username>/seedsigner-translations

Click into the `l10n/<language_code>/LC_MESSAGES` folder.

`<language_code>` will be "es" for Spanish, "pt_BR" for Brazilian Portuguese, etc.

You should see a messages.mo and messages.po file. In the upper right click "Add file" and choose "Upload files":

<img width="600" alt="Screenshot 2025-01-13 at 3 51 22 PM" src="https://gist.github.com/user-attachments/assets/807a1b2d-8df8-4a3e-b671-49c72a903ede" /><br/>

Verify that the following screen is listing the correct directory (you should be within the LC_MESSAGES folder for your language!):

<img width="800" alt="Screenshot 2025-01-13 at 3 54 38 PM" src="https://gist.github.com/user-attachments/assets/b3b34d90-6715-4e08-87aa-ac395f632f0c" />

* Click to upload your `messages.po` file.
* Select "Create a new branch for this commit and start a pull request."
* Name your new branch with the language code and date: e.g. `es_2025-01-13`
* Click "Propose changes".

On the following screen we will finalize your Pull Request (PR):

<img width="800" alt="Screenshot 2025-01-13 at 4 02 20 PM" src="https://gist.github.com/user-attachments/assets/f6c21233-53bf-495e-9695-1b38b2e51299" />

* Click on "compare across forks". That will alter the "base repository" droplist options.
* Select "SeedSigner/seedsigner-translations" as the "base repository".
  * Its "dev" branch should already automatically be selected.
* Add a title that includes the language code and (optional) additional context/info.
* Scroll down and review the diff at the bottom.
  * If you spot any translations issues, you can only fix them back in Transifex. After any issues are fixed, you'll have to download the `messages.po` file and repeat this process.
* Click "Create pull request" when you're ready.

---

### Review new/updated screenshots
Once your PR is created, you'll see the results of our automated checks:

<img width="612" alt="Screenshot 2025-05-01 at 11 02 04 AM" src="https://gist.github.com/user-attachments/assets/1970d974-4241-4155-923f-ff637cc5f84f" />

Click into "All checks have passed" to reveal the "CI / test (pull_request)" line. Click on that to view the details.

<img width="853" alt="Screenshot 2025-05-01 at 11 05 01 AM" src="https://gist.github.com/user-attachments/assets/c87861ea-5f82-4439-adc7-9900c3943a9c" />

Click "Summary" and scroll down to the "Artifacts" section:

<img width="1025" alt="Screenshot 2025-05-01 at 11 07 28 AM" src="https://gist.github.com/user-attachments/assets/3bcb1b0e-dd7e-4944-a728-af8cacc91d6f" />

Click the download arrow to download a zip file of the results.

Inside you'll see:

<img width="180" alt="Screenshot 2025-05-01 at 11 09 41 AM" src="https://gist.github.com/user-attachments/assets/918d0590-e87e-4fce-a62c-cd62cf6ce034" />

Double click on the "index.html". This will open the "Screenshots Diff Report" in your browser. It will show a before/after of all screens that have been changed. It will also display new screens that were added and display any that were removed (adding or removing screens would only result from core codebase changes OR if you're adding a brand new language for the first time).

It is up to you to review this diff report and visually inspect the impact your translation have had on the listed screens.

We expect that many translations will need adjusting. The point of the Screenshot Diff Report is so that you can quickly identify problem translations and immediately return to Transifex to revise them.

---

### Which text can run offscreen and which cannot?

Okay to run long:
* Titles
* Buttons

![ToolsDiceEntropyMnemonicLengthView](https://gist.github.com/user-attachments/assets/69fcadc6-5706-4877-9676-f70768c0f576)

In this screenshot both the title and the active button will scroll the text back and forth into view. Better to avoid if possible, but totally acceptable if either require scrolling.

NOT okay to run long:
* Warning screen subheads
* Any other body content

![SeedTranscribeSeedQRWarningView](https://gist.github.com/user-attachments/assets/7b06d4ac-580e-4a66-9161-acf1a3b6b5cb)

Notice that the red subheader text does not fit. These subheads do NOT currently autoscroll.


![SeedExportXpubWarningView](https://gist.github.com/user-attachments/assets/1a2ee6e6-8a2b-4c4c-a5c1-74a528333ac1)

Any text that runs too long vertically and ends up offscreen or obscured by another screen element would need to be rewritten to be shorter.



---

### Submitting revised translations to your existing PR
If a screenshot does reveal a problematic translation, make your translation edits in Transifex, then repeat the process of downloading the translation file.

Then at the top of your PR, click into your fork's branch:

<img width="1016" alt="Screenshot 2025-05-01 at 11 21 33 AM" src="https://gist.github.com/user-attachments/assets/422fad5e-3837-4e1f-b1b7-6c36bc461b93" />

Then follow the same steps from "Upload your changes to your fork" above to navigate to the proper folder and then "Upload files". Once again, select your `messages.po` file.

The only difference this time through is that this will be treated as an additional commit on top of the one you did earlier. Once the updated file is committed, your PR will automatically include the latest changes.

At this point the automated system will re-run itself and generate a new Screenshot Diff Report for you to download and review.

Repeat this process as many times as necessary until you're satisified with all screens in the Screenshot Diff Report.

---

### What happens next?
Now that your PR is created, the project maintainers will review your PR and either merge your changes into the main translations repo or request changes.

Merged changes will then be included in the next SeedSigner release.