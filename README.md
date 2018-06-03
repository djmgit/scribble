## Scribble CLI

[![IMAGE ALT TEXT](http://img.youtube.com/vi/NsqwQYdDa28/0.jpg)](http://www.youtube.com/watch?v=NsqwQYdDa28 "Using scribble from terminal")

## What is Scribble

Scribble is primarily a terminal based note taking application for devs. It allow us to create notes, view existing notes, search existing notes, delete notes from the terminal itself. We can take note while working on terminal without switching to any other web based or desktop based application.

Scribble CLI used [Scribble API](https://github.com/djmgit/scribble_api) as the backend API for data and auth services.

## Setting up Scribble

Scribble CLI, as of now has to be built from the source. It is extremely easy and can be seen below :

- Clone this repo or clone your own copy after forking.
- Enter into the repository and open in terminal.
- Execute ```python setup.py install```. You may have to provide superuser access.

Scribble will be installed on your system.

## How to use

Once the application has been installed, you need to first register yourself with scribble. This is extremely easy.
Just execute the following:

```
scribble register

Enter username : testuser
Enter password : 
Retype password :

```

The register command will ask for username and password. Please provide those and you will be successfully registered.

Once you are registered, you will have to login using the following command.

```
scribble login
```
Once again it will ask for your username and password. Provide the proper username and password and you will be logged in.

```
Enter username : testuser
Enter password : 
Logging you in...
You have been successfuly logged in
Scribble executed successfully!

```
Now you are all set to go!

### Creating notes

To create a new note, you will require the ```scribble note ``` command. Use ```scribble note -h``` to know all the
possible options. The simplest way to create a note is as follows : 

```
scribble note -t 'scribble is fun' -k 'testing' -c 'beginner'
```
This will open your default edittor like nano or vim, type your content there. Once done, a new note with title (specified
using -t, keywords specified using -k and category specified using -c) will be created. Specifying a note title is a must, so
even if you forget specifying that, you will be later asked to specify a note title.

The response is given below :

```
saving your note...
Your note has been save successfully!
Scribble executed successfully!
```

### Viewing notes

Viewing notes is also very easy. You can view all notes using ```scribble view``` command.

```
scribble view
Retrieving your notes...

|   Note id | Note                                  |
|-----------+---------------------------------------|
|        11 | this is a note from command line      |
|        12 | this is another note from terminal    |
|        14 | app is packaged                       |
|        15 | app is deployed                       |
|        17 | this is from extension                |
|        18 | this is another from chrome extension |
|        19 | scribble is fun                       |

```

Inorder to view the details of a particular note, just mention the note id of that note.

```
scribble view -i 19

Retrieving your note...


#19 scribble is fun
====================================================================


This is anoter note.



Keywords : testing


category : beginner

```

### Searching notes

You can always search existing notes for a given word or phrase. All the notes containg your search phrase will be filtered
and shown to you. Notes can be searched using the ```scribble search``` command.

```
scribble search -p nano

|   Note Id | Note Tile                          | Note Body                                    | Keywords    | Category   |
|-----------+------------------------------------+----------------------------------------------+-------------+------------|
|        11 | this is a note from command line   | this is from nano, cool right?               | fun         |            |
|        12 | this is another note from terminal | This is yet another from nano, oh yeahhhhh!! | fun,fun,fun |            |

```
Using the search command with a search phrase specified by the -p siwtch, all the fields of all the notes are searched for a
match. However if we want to search in only particular fiels, then we can mention those fields separately.

```
 scribble search -p 'packaged' -f 'note_title,note_body'
 
|   Note Id | Note Tile       | Note Body                                               | Keywords   | Category  |
|-----------+-----------------+---------------------------------------------------------+------------+-----------|
|        14 | app is packaged | The app is now packaged and can be installed using p... |            |           |





