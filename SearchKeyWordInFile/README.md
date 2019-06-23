# SearchKeyWordInFile

## About
This is a small project used to solve the problem that when something important suddenly into our mind, we want to make sure but don't know where it is expect the directory. By this time, we can use this project to search the directory by keyword and it will return the abosultely path of the file which contains the keyword.

## Remind
There are still some errors and warnings in this project that I couldn't slove.
1. when handling pdf file, it will throw some warnings.
2. when handling doc file, it will throw the error `java.lang.NoSuchMethodError`. However, I test it works fine when I write a test unit. It just goes wrong then I call it in another package.

## Dependency
It needs you import `POI` and `pdfbox` first.
Maybe the `org-apache-commons-logging.jar` is also needed.
Here are the jars I uses:
```
poi-3.17.jar
poi-ooxml-3.17.jar
poi-scratchpad-3.17.jar
xmlbeans-2.6.0.jar
commons-collections4-4.1.jar
poi-ooxml-schemas-3.17.jar
org-apache-commons-logging.jar
fontbox-2.0.11.jar
pdfbox-2.0.11.jar
```

## Usage
It is easily to use except you should import the reliable jar package first.
You should input the keyword first then select the directory. This is very important cause they're turn couldn't be reversed.

## Last
I'm a newbie in program, feel free to point out my problems.