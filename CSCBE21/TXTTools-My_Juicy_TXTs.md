1# Context 
Now that we know that TXTTools is insecure, I don't want my juicy TXTs all over the internet. Can you try to get some system credentials so that I can remove my juicy TXTs? Maybe try another part of the site as they might have fixed the previous issue.

http://54.78.53.55/

2# Solving 

When you arrive on the website, you notice multiple buttons on the top of the website that redirect to different features (which tanslates in different ports in the URL). One of the buttons is disabled though : the merging files one. You can make it available through the developper tools or directly access the page throgh the port 8888.   

There you can upload zip files and the page shows you the content of the texts that are in the zipfile. Therefore we will do a zip slip attack. To exploit the directory traversal we will use this command : 
``` ln -s ../../../../../../../etc/shadow shadow ```  

You then need to zip the 'shadow' file just created. Upload it on the website and it will show you the flag. 
