# Error detection and correction: dealing with homophone confusion

In written language, errors involving the use of words that sound similar or the same are fairly common. For example, the word its is frequently used where it's should, and vice-versa. Other confusable pairs include: they're/their/there, you're/your and loose/lose.

Develop an approach for detecting and correcting errors for the following specific types of confusion (in either direction):

    it's vs its
    you're vs your
    they're vs their
    loose vs lose
    to vs too
    
Given a text file create a new text file that differs only from the input file in which errors are corrected.

For example, given a file containing:

    Then pour water or light oil from a graduated beaker into the chamber to 
    fill the chamber too its gasket surface. The horses moved at a clump; they
    were no more on parade than was they're driver; one fork of the road was as 
    good as another. 
    
Turn into a new text file containing:

    Then pour water or light oil from a graduated beaker into the chamber to fill the chamber to its gasket surface.
    The horses moved at a clump; they were no more on parade than was their driver; one fork of the road was as good as          another.
    
There may be zero, one or more corrections required per line.

##Data, tools, etc.

You may use open-source tools, libraries and toolkits (e.g. NLTK, Stanford CoreNLP). However, you may not use any commercial software or any free software for which source code is not provided.

Test file may contain text of different genres, and errors are expected to be distributed differently. As a result, performance on the sample data may or may not match performance on the test set.
