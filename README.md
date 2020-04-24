# batch-tiff-2-pdf

Basically just a small script I modified because at work I need to convert a mix of searchable/unsearchable .pdf's to all searchable. Over 30,000 of them... And I don't have Adobe Acrobat so, as far as I'm aware, I have no "force-OCR" capabilities. 

So, the solution was to convert all the .pdf's to .tiff's, eliminating any searchable text within the document, and then convert back to .pdf's from .tiff's. 

The only downsize is the filesizes are much bigger when converting back from .tiff's but I'm scared to lose image quality, potentially neudering OCR. And, with 30k documents to process tomorrow, I'm not going to risk it.

I won't be storing the .pdf's, I'll be scraping them of their data so I can reference certain key's unique to various .pdf's. Someone put them in the wrong folders :(

Hope this helps!