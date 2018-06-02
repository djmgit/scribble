## Scribble CLI

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


