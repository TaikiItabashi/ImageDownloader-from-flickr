ImageDownloader.py : Get the "imageURL List" , "tag List" and "extra meta data" from Flickr.
	��Enter the three parameters after running the program.
		1 : Search word(A Single Word)
		2 : the number of acquisition
		3 : the recent shooting date and time
			��get back from entered date
			��It required by the specifications of the API when get more than 4000.
			
	Output:
		./[Search word]/imgURL.txt 						: ImageURL List
		./[Search word]/data/[*****]_[*****].txt		: Tag List
		./[Search word]/data/[*****]_[*****] etc.txt	: extra meta data
		
After runnning ImageDownloader.py... 
Please get image using download manager such as "Irvine" from Image List.