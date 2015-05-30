# Impossible Questions

I was recently asked to interview for a very well known software company. I'm definitely still a junior dev (and I was clear about this)
 but I was super excited for the opportunity (crazy awesome perks!) and ready for some fun programming challenges. 
 I'm not an expert programmer by any stretch, but boy do I enjoy solving problems.
 
  
So, that gives us our first lemma: One bit can only store two states: 1 and 0. 

    Lemma A: Given two possible states (0 and 1) we can only represent two states:

    Proof:
        We state all possible cases and count them.
        Case one: 0
        Case two: 1 ∎

That's great! Well, what if we add a second bit? It turns out that this doubles our capacity for storage. For 
those of you who know binary this is painfully obvious: two bits gives us four states, three gives us eight, and so on:
    
    
    Remember, 0 is a state too!
    
    4 + 2 + 1 = 7
    1   1   1 = 7 (in binary!)
    
    
The binary number 111 gives us more information than three unique bits could. 
The reason for this is that the _position_ of the bits is another way to store information. As we change position in
 binary we aren't increasing the amount of storage by an order of ten as we would in decimal, but instead by an order of two.

Thus, our second lemma: For each added binary bit we double the total amount of information that we can store. 

    Lemma B: For each additional position allowed (n) in a base b numbering system, you are increasing the storage by a factor
        of b. 
            -> Storage = S = b^n

    Proof:
        We know by the [Rule of Product](http://en.wikipedia.org/wiki/Rule_of_product) that the possible combinations 
        of any number of sets is the product of the size of those sets. For example, to choose one of {1,0} 
        and one of {1,0} is to have one of {11,01,10,00}.
        The size of our sets is the number of possible choices of numbers for our base: b
        The number of sets is the number of positions we allow ourselves: n
        Thus, we multiply b by itself n number of times giving us: b^n total possible combinations.
        Knowing that we multiply b by itself, we know we are increasing the total capacity for storage by a factor of b 
        for each additional number position allowed ∎
        
  
Now it looks like we're getting somewhere! But, do we _always_ need all those bits? Can't binary 10000000000 somehow be cleverly 
 represented as 1 with 1010 zeros? Can't every number?


As it turns out, if we were to randomly generate a fixed amount of bits,
 and then we were to try to come up with a way to represent that _same_ information but using fewer bits (compress them)
 , we wouldn't be 
 reducing the size of our number very much at all. It's always possible that we could find numbers that give us interesting patters:
 perfect squares (or close to them), numbers with a large sequence of zeros (scientific notation) and so on. However,
 on average (if we have no control of the numbers we get), we will need the same amount of bits to represent our 
 information no matter the compression chosen: Shannon covered this in his famous paper: [A Mathematical Theory of Communication](http://cm.bell-labs.com/cm/ms/what/shannonday/shannon1948.pdf). 
  
 For our purposes we can build our third assertion: When given some bits we won't be able to significantly reduce the 
 amount of bits without losing information.
  
  
 So that covers that so far! What does this have to do with programming interviews? Well, it turns out our problem to solve
  was, in a way, related to Shannon's Limit.
   
   
__The scene:__

A person in their livingroom opens their TV guide. They notice on the left of the guide is a series of numbers in decimal,
  all listed under a column titled _"Record Code."_ Interested in what this means, this person calls up the company 
  responsible for the TV guide and gets a support representative on the phone.
  
"Hello! Thank you for calling TV Guide Co. My name is John. How can I help you?"

The man gives his query, which drives the support representative into a sales pitch to sell their awesome new VCRs with 
smart-recording! Just plug the number and the VCR starts recording for you!
 
 _Awesome!_ But how does it work?
 
 Well, actually, a lot of people spent some really good time backwards-engineering this very problem. There is a thing
 called VCR-Plus that existed for this very function. It was a real product and it _worked!_ 
 
