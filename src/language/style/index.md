(documentation-style-guide)=
# Style guide

This chapter describes the style guide for our documentation. We will cover the conventions 
for writing the technical documentation.


## Organization


The documentation is divided into **books**, **parts** (labeled `part:`), **chapters** (labeled `chapter:`), 
and **sections** (labeled `sec:`).

The structure of each book is stored inside the `src/_toc.yml` file.



## General guidelines for technical writing

The following holds for all technical writing.

- The documentation is written in correct English.

- The words "should" and "must" are not interchangeable, they have precise meanings;[^rfc2119]

[^rfc2119]: These meanings are explained [in this document](https://www.ietf.org/rfc/rfc2119.txt).

- "Please" is unnecessary in technical documentation;
  ```{admonition} Wrong
  :class: danger

  "Please remove the SD card."
  ```
  
  ```{admonition} Better
  :class: success

  "Remove the SD card."
  ```

- Do not use colloquialisms or abbreviations;
  ```{admonition} Wrong
  :class: danger

  "The pwd is `ubuntu`."
  ```

  ```{admonition} Better
  :class: success

  "The password is `ubuntu`."
  ```


- Python is capitalized when used as a name;
  ```{admonition} Wrong
  :class: danger
  
  "If you are using python..."
  ```
  
  ```{admonition} Better
  :class: success
  
  "If you are using Python..."
  ```



- Do not use contracted forms;
  ```{admonition} Wrong
  :class: danger
  
  it's
  ```

  ```{admonition} Better
  :class: success
  
  it is
  ```


- Do not use emojis;

- Do not use **ALL CAPS**;

- Make infrequent use of **bold statements**;

- Do not use exclamation points;



## Style guide for the Duckietown documentation

- The English version of the documentation is written in American English;
  ```{admonition} Incorrect
  :class: danger
  
  behaviour
  ```

  ```{admonition} Correct
  :class: success
  
  behavior
  ```

- All the filenames and commands must be enclosed in code blocks using Markdown backticks;
  ```{admonition} Incorrect
  :class: danger
  
  "Edit the ~/.ssh/config file using nano."
  ```

  ```{admonition} Correct
  :class: success
  
  "Edit the `~/.ssh/config` file using `nano`."
  ```

- <kbd>Ctrl</kbd>-<kbd>C</kbd>, `ssh`, etc. are not verbs;
  ```{admonition} Incorrect
  :class: danger
  
  "<kbd>Ctrl</kbd>-<kbd>C</kbd> from the command line."
  ```

  ```{admonition} Correct
  :class: success
  
  "Use <kbd>Ctrl</kbd>-<kbd>C</kbd> from the command line."
  ```

- Subtle humor and puns about duckies are encouraged.



## Frequently misspelled words

- "Duckiebot" is always capitalized.

- Use "Raspberry Pi", not "PI", "raspi", etc.

- These are other words frequently misspelled:

  5 GHz
  WiFi


## Other conventions

When the user must edit a file, just say: "edit `/this/file`".

Writing down the command line for editing, like the following:

    $ vi /this/file

is too much detail. Only specify the editor to use if the task at hand requires 
functionalities that are only available on a specific editor.


## Troubleshooting sections

Write the documentation as if every step succeeds.

Then, at the end, make a "Troubleshooting" section.

Organize the troubleshooting section as a list of symptom/resolution.

The following is an example of a troubleshooting section.


### Troubleshooting

Use the [`{trouble}` directive](language-format-troubleshooting) to declare troubleshooting
steps. For example,

```{trouble}
This strange thing happens.
---
Maybe the camera is not inserted correctly. Remove and reconnect.
```
