# Python
if you want to view it offline download the html file attached as ```Python.html```

<body><article id="de65cb3d-a9bf-48ec-9266-f2837e839091" class="page sans"><div class="page-body"><blockquote id="4e0190be-741c-47d6-af93-e435722b4e0a" class="">Python is an interpreted, object-oriented, high level programming language with dynamic semantics.</blockquote><figure class="block-color-gray_background callout" style="white-space:pre-wrap;display:flex" id="1165721a-0181-43dd-9d93-26664be64615"><div style="font-size:1.5em"><span class="icon">💡</span></div><div style="width:100%"><strong>interpreted </strong>= code doesn&#x27;t stop until found error, if found error on last lines the above code gets executed.
<strong>object-oriented </strong>= works on the concept of &#x27;object&#x27; which can contain data and code
<strong>high level </strong>= made in that way that everyone can understand (simple syntax)
<strong>dynamic semantics </strong>= will know what kind of data structure(int, char) is passed in a variable when starts running.</div></figure><hr id="b9a196e7-b276-4935-907e-6285547622fe"/><h2 id="763690a6-04e4-4a12-badf-a0b3462c095a" class=""><details open=""><summary><strong>Data types</strong> </summary></details></h2><div class="indented"><figure class="block-color-gray_background callout" style="white-space:pre-wrap;display:flex" id="5461055f-3fbd-486d-bab4-b6788d6d4ed2"><div style="font-size:1.5em"><span class="icon">💡</span></div><div style="width:100%">type() use check the datatype of a variable</div></figure><figure class="block-color-gray_background callout" style="white-space:pre-wrap;display:flex" id="1706ea58-ef63-4a94-b891-a003ec3c229d"><div style="font-size:1.5em"><span class="icon">💡</span></div><div style="width:100%">mutable object can change its state or contents and immutable objects cannot
-- <strong>Mutable datatypes -- list , dictionary , byte array , set
-- Immutable datatypes -- int , float , complex , string , tuple</strong>.</div></figure><figure class="block-color-gray_background callout" style="white-space:pre-wrap;display:flex" id="ffc2e32d-f360-484d-8238-5dc272fa2ffa"><div style="font-size:1.5em"><span class="icon">💡</span></div><div style="width:100%">changing the type of a data type is known as &quot;Type Casting&quot;-- int(), float(), eval()[eval can handle int, float and binary too].</div></figure><ol type="1" id="aaf2c726-18a7-4615-9d00-c184367ecb5d" class="numbered-list" start="1"><li><strong>Numeric</strong> --
<strong>integers </strong>(57) ,
<strong>float</strong> (57.7) ,
<strong>complex </strong>numbers (5 + 7j)</li></ol><ol type="1" id="6d11a763-fca0-4179-b08b-04a26eeea4bf" class="numbered-list" start="2"><li><strong>Sequence</strong> --
<strong>string </strong>(<code>&#x27;hi&#x27;, &quot;hello&quot;, &#x27;&#x27;&#x27; hey &#x27;&#x27;&#x27;</code>) (putting addition sign between strings makes it CONCAT //<code> &#x27;10&#x27; + &#x27;20&#x27; = &#x27;1020&#x27;</code>),
<strong>list</strong> ( <code>l = [1,57.7,&#x27;sw&#x27;]</code>)( <code>l[1] = 57.7</code> ) ,
<strong>tuple</strong> (<code>1,57.7,&#x27;sw&#x27;,1+5j</code>)(same as list but immutable)</li></ol><ol type="1" id="395e46c3-0838-4f59-8113-1e5e7804ddab" class="numbered-list" start="3"><li><strong>Dictionary</strong>
(<code> d = { key: &#x27;value&#x27; , &#x27;name&#x27;: &#x27;python&#x27; , 3:3 }</code>)(key has to be unique) ( d[&#x27;key&#x27;] = &#x27;value&#x27;)</li></ol><ol type="1" id="9f2f9abc-46f3-4b96-b758-fabfc2b96747" class="numbered-list" start="4"><li><strong>Set</strong>
( <code>s = {1,2,3,4,5,6}</code>)(every value is unique in curly brackets)</li></ol></div><hr id="bd5cd6bf-f4b1-410b-8ee5-64e7a4d98d38"/><h2 id="290f8a44-ef22-40d5-84cf-9920ac754d0c" class=""><details open=""><summary>Operators in python</summary></details></h2><div class="indented"><ol type="1" id="054a803f-8847-41d3-9dab-68b1b725e83e" class="numbered-list" start="1"><li><strong>Arithmetic operators</strong>
(<code> +, -, *</code><code><em>, /, % </em></code><em>(modulus)(remainder),
** (exponents)(5 ** 3 = 5</em>5*5 = 125),
// (floor division)(10 // 3 = 3.3333 = 3))</li></ol><ol type="1" id="5d3962a4-8639-4ace-a7c4-5bbd9982dae2" class="numbered-list" start="2"><li><strong>Assignment</strong> <strong>operators</strong>
(<code> =, +=</code> (&#x27;x += 3&#x27; = &#x27;x = x + 3) ,
<code>-=</code> (&#x27;x -= 3&#x27; = &#x27;x = x - 3) )</li></ol><ol type="1" id="2aa96d51-e4c4-41a7-a187-381e11b621ac" class="numbered-list" start="3"><li><strong>Comparison</strong>
(<code> == , != , &gt; , &lt; , &gt;= , &lt;= </code>)</li></ol><ol type="1" id="48628e9c-b066-4a56-8fd8-45606a7f93e9" class="numbered-list" start="4"><li><strong>Logical</strong>
( <code>and </code>(return true if both statement are true)(x&lt;5 and x&lt;10),
<code>or</code> (return true if one is true),
<code>not</code> (return false if both are true)(&#x27;not(x&lt;5 and x&lt;10)&#x27;))</li></ol><ol type="1" id="36e4008a-31ec-49e0-9fa8-da020b3c4fe9" class="numbered-list" start="5"><li><strong>Membership</strong>
( <code>in </code>(return true if present in object) ,
<code>not in</code> (return true if not present in object))</li></ol><ol type="1" id="90404d95-ca6a-49e1-95e3-55fc360d441d" class="numbered-list" start="6"><li><strong>Identity</strong>
( <code>is </code>(return true if both variable are same), not is (opposite))</li></ol><ol type="1" id="f5f689b9-2c04-41d4-902b-5b85c63230de" class="numbered-list" start="7"><li><strong>Bitwise</strong>
(<code>&amp;</code><strong> </strong>(and) , <code>|</code> (or) , <code>^</code> (xor)) [bin() to change int to binary]</li></ol></div><hr id="bc66f1d5-4461-4c22-90de-9722252a0eb0"/><h2 id="05d3fb58-63f4-423c-a5b5-f02905a65fe4" class=""><details open=""><summary><strong>String functions</strong></summary></details></h2><div class="indented"><blockquote id="9628f329-d20b-4b53-90b3-63c80e0c46e9" class="">anything in between quotes is string </blockquote><p id="ac1dddf0-1523-4ee7-967f-c574127ea216" class=""><code>s = &quot;Welcome&quot;, x = &quot;Welcome123&quot;, y = &quot;5757</code>
<code>lower()</code> (makes a string in lower case)
<code>upper()</code> (upper case)
<code>title()</code> (makes every word&#x27;s first letter capital)
<code>capitalize()</code>  (makes first letter upper and every other lower case)
<code>find()</code>  (<code>s.find(&#x27;e&#x27;)</code> =&gt; 1) (gives the index of first found) (<code>s.find(&#x27;e&#x27;,2) </code>=&gt; 6) (gives the second &#x27;e&#x27; after giving start para.) (if not found will return &#x27;-1&#x27;)
<code>index()</code>  (<code>s.index(&#x27;e&#x27;)</code> =&gt; 1) (if not found will return &#x27;Error&#x27;) (we can give 2nd para.)
<code>isalpha()</code>(<code>s.isalpha() </code>=&gt; true) (<code>x.isalpha()</code> =&gt; false -- because it contains numeric digit)
<code>isdigit()</code>(<code>x.isdigit() </code>=&gt; false -- because it contains alphabets) (<code>y.isdigit()</code> =&gt; true)
<code>isalnum()</code>(checks if the string contains special characters) (if contains then false else true)
<code>chr()</code>(convert int to ASCII character) (<code>chr(65)</code> =&gt; &#x27;A&#x27; =&gt;<code> type(&#x27;str&#x27;)</code>)
<code>ord()</code>(opposite of chr()) (<code>ord(&#x27;A&#x27;)</code> =&gt; 65 =&gt; <code>type(&#x27;int&#x27;)</code>)</p><ul id="2034819c-43ac-4cae-a346-84bc88408f7d" class="toggle"><li><details open=""><summary><code>format()</code> --  string formating</summary><pre id="93160be8-cdc2-46b6-8664-21bdef868e30" class="code"><code>named indexes
txt1 = &quot;my name is {fname} {lname}&quot;.format(fname=&#x27;tabish&#x27;,lname=&#x27;shaikh&#x27;)

#numbered indexes
txt2 = &quot;my name is {0} {1}&quot;.format(&#x27;tabish&#x27;,&#x27;shaikh&#x27;)

#empty indexes
txt3 = &quot;my name is {} {}&quot;.format(&#x27;tabish&#x27;,&#x27;shaikh&#x27;)</code></pre><pre id="d573ee53-cfb0-4503-b485-3db5ed4472cb" class="code code-wrap"><code>#Output
#All output will be =&gt; &quot;my name is tabish shaikh&quot;</code></pre><figure class="block-color-gray_background callout" style="white-space:pre-wrap;display:flex" id="7d6fd6d9-cc5e-4b82-9f6e-1da80e815051"><div style="font-size:1.5em"><span class="icon">💡</span></div><div style="width:100%"> if we put it like this {a:10} then the output will take 10 char. space from left
 if we put it like this {a:^10} then the output will take 10 char. equal space from both sides
 if we put it like this {a:&gt;10} then the output will take 10 char. space from right</div></figure></details></li></ul></div><hr id="460bc394-b86e-4861-8fab-f42dc3e3e1c3"/><h2 id="2e8a808c-2588-4dff-b9ea-983836437f29" class=""><details open=""><summary><strong>List</strong></summary></details></h2><div class="indented"><blockquote id="771e6669-6360-4593-bd38-db604cd882f0" class="">- if list contains another list then its known as &quot;Nested list&quot;</blockquote><pre id="fa5773c0-ee07-4fe1-bb5c-e88b0debaabe" class="code"><code>l = [1,2,3,[4,5,6]]
l[1] = 2
l[3] = [4,5,6]
l[3][2] = 5</code></pre><hr id="a6c78b33-6331-4e07-8d70-d5b13a22e4eb"/><h3 id="fd21aa43-8ebc-4892-bd08-4b1d26994803" class=""><details open=""><summary><strong>slicing of list</strong></summary></details></h3><div class="indented"><pre id="11f4b396-810b-4b91-938f-e591f6fc891a" class="code"><code>l = [2,3,&#x27;Hello&#x27;,[3,4,5]]
l[0:2] = [2,3]
l[0::2] = [2,&#x27;Hello&#x27;]
l[-1] =  [3,4,5]
l[-1::-2] = [[3,4,5],3]
l[-1::-1] = [[3,4,5],&#x27;Hello&#x27;,3,2]</code></pre></div><hr id="42f55bb9-fa1e-42d9-8aef-822a42a1208e"/><h3 id="0d194518-f252-429b-b5fc-c8a21082b73f" class=""><details open=""><summary><strong>List Iteration</strong></summary></details></h3><div class="indented"><pre id="1c635372-73a9-4241-bbd9-aa8b655e6e81" class="code"><code>l = [10,20,30,50,60]
t = len(l)
for i in range(t):
	print(l[i])</code></pre><pre id="82978bba-c66c-4aa9-ad3b-3660cc1a803c" class="code"><code>l = [10,20,30,50]
t = len(l)
for i in range(t-1,-1,-1):
	print(l[i])</code></pre></div><hr id="d60186ba-8311-47c3-8b30-6ec69dbeccb7"/><h3 id="22f72694-fe64-4590-95eb-bcf318a9e620" class=""><details open=""><summary><strong>List function</strong></summary></details></h3><div class="indented"><p id="f33ac723-d6a4-4afc-9475-4a09cd9680db" class=""><code>l = [10,20,30,50]</code>
<code>del </code>-- del needs list name and index to delete it (<code>del l[1]</code>)
<code>pop()</code>-- same as del but also return the delete character (<code>l.pop(2)</code>)
<code>remove()</code> -- it needs value to delete instead of index (<code>l.remove(50)</code>)
<code>clear()</code> -- makes blank(delete) the whole list <code>(l.clear()</code>)</p><p id="28026ea3-4476-4d54-a12e-1688f39b4e73" class=""><code>insert()</code> -- inserts the value to given index (<code>l.insert(0,5)</code>) <code>insert(index,value)</code> and pushes other value to +1 index and to work on if indexes is 4 and passes 5
<code>append()</code> -- added the value in last of list (<code>l.append(60)</code>) if passes another list in append then makes it nested list
<code>extend()</code> -- same as append but when passes list it doesn&#x27;t make nested list picks one by one value and added it</p><p id="a0177fef-3323-41b9-a0c7-0a0ff909a406" class=""><code>count()</code> -- counts the value in list (<code>l.count(10)</code>)
<code>max()</code> -- gives the maximum value in list (<code>max(l)</code>)   this also works for alphabets
<code>min()</code> -- gives the minimum value in list (<code>min(l)</code>)   this also works for alphabets
<code>sort()</code> -- update and sorts the list in ascending order (l<code>.sort()</code>)
<code>reverse()</code> -- update and reverse the given list (<code>l.reverse()</code>)
<code>index()</code> -- gives the index of passed value (<code>l.index(20)</code>)</p></div><hr id="70ad80cf-5644-4084-804a-d884c3cba4f2"/><h3 id="942c1713-753b-4c9b-aecb-d09080171af8" class=""><details open=""><summary>List Comprehension</summary></details></h3><div class="indented"><p id="6da4f298-f5da-4b53-b44e-fde6b8091b8d" class=""><code>n = [i for i in range(1,101)]</code>       =&gt; n = [1,2,3,.....,99,100]
<code>n = [i for i in range(1,101) if h%2 == 0]</code>       =&gt; n = [2,4,6,8,10,....,98,100]</p><p id="3a8f8fc9-7957-4303-bbc4-e7c105bccc60" class=""><code>s = &#x27;Tabish&#x27;</code>
<code>n = [g for g in s]</code>      =&gt; n = [T,a,b,i,s,h]</p></div><hr id="559751f6-bced-4a48-a448-e63ff5bb6163"/><h3 id="2c14c828-5aeb-4333-87ab-376143cd19b8" class=""><details open=""><summary>Zip function</summary></details></h3><div class="indented"><blockquote id="149e757d-2c7d-40f2-be73-81b97beb5ec0" class="">iterate two same list at a same time</blockquote><pre id="3ffbb6dd-938a-4a7f-9a1b-9b46b57a7bdf" class="code"><code>l =[10,20,30,40]
ll =[98,54,33,53,43]
t = len(l)
for a,b in zip(l,ll):
	print(a,b)

for h in range(t):
	print(l[h],ll[h])</code></pre><figure class="block-color-gray_background callout" style="white-space:pre-wrap;display:flex" id="1dbc8577-06f0-41d5-8aa7-1a1e9220457c"><div style="font-size:1.5em"><span class="icon">💡</span></div><div style="width:100%">#output
10 98
20 54
30 33
40 53</div></figure></div><hr id="0477a0ca-f749-4f09-9ee6-2f7bce82bffe"/><h3 id="a88df55d-2599-4be0-bcb3-90ffa7e8e1aa" class=""><details open=""><summary>string to list</summary></details></h3><div class="indented"><p id="5d93d392-a31c-4643-95e4-c06046c09d50" class=""><code>split() </code>-- makes a string to list gives comma on every space.
<code>n = &#x27;md tabish shaikh&#x27;</code>
<code>l = n.split()</code> =&gt; [&#x27;md&#x27;, &#x27;tabish&#x27;, &#x27;shaikh&#x27;]</p><pre id="8d0327e4-8186-46bf-9254-f9cf1a410b07" class="code"><code>l = []
for a in range(1,4):
	n = input(&#x27;Enter the value &#x27;+str(a)+&#x27; :-&#x27;)
	l.append(n)
print(l)</code></pre></div></div><hr id="53e1ec73-3d3a-4a40-ac97-bfdeffca9784"/><h2 id="77962a2e-7cd9-4ac8-89b8-474ca2213b10" class=""><details open=""><summary>Stack</summary></details></h2><div class="indented"><blockquote id="5f850044-6067-4bb4-9b85-ac2ec50f96e0" class="">Stack is a linear data structure just like books on top of books</blockquote><blockquote id="5af8df06-c6d7-42a7-9cd9-cab8d6625e59" class="">stores item in Last-in/First-out (LIFO) or First-in/Last-out (FILO) manner</blockquote><p id="64757e06-67e0-4d36-8c79-77b8e0ca8dea" class=""><strong>push</strong><code> </code>-- inserting an element -- <code>append()
</code><strong>pop()</strong> -- deletion of last element -- <code>pop()</code>
<strong>peek </strong>-- display the last element -- <code>l[-1]</code>
<strong>display </strong>-- display list -- <code>print(l)</code>
<strong>exit </strong>-- to exit --  <code>break</code>;</p></div><hr id="94b9b6b6-6393-4d10-9765-9e4a4e614227"/><h2 id="c2ecde76-db03-4596-94c1-c67a46a55855" class=""><details open=""><summary>Queue</summary></details></h2><div class="indented"><blockquote id="03ebdfa4-d11f-493f-a22d-979ecc758c16" class="">Queue is a linear data structure just like a queue for ticket in railway station</blockquote><blockquote id="eb1e01de-3763-479a-8fb0-ed9d339bd261" class="">stores item in First-in./First-out (FIFO) manner</blockquote><p id="93e43a32-c7e1-4d72-8851-0f634451c236" class=""><strong>Enqueue </strong>-- Adds an item to queue -- <code>append()</code>
<strong>Dequeue</strong> -- Removes an item from queue -- <code>del l[0]</code>
<strong>Front </strong>-- Get the front(1st) item from queue -- <code>l[0]</code>
<strong>Rear</strong> -- Get the last(last) item from queue -- <code>l[-1]</code></p></div><hr id="3f72c754-b0b9-4efb-8fc4-74f46e15fc0c"/><h2 id="d1a1c403-72b2-4065-b84d-641fed85bb30" class=""><details open=""><summary>Dictionary</summary></details></h2><div class="indented"><blockquote id="69ca1648-da4e-4ac8-81c2-23214424f5a3" class="">Dictionary is a Unordered datatype, It is Mutable, Index doesn&#x27;t work in dictionary</blockquote><blockquote id="c7501c37-ac0a-470a-a31b-957fbe9e0949" class="">key : value -- key is unique</blockquote><blockquote id="058afc9c-2d30-4775-94c7-c450beea0f13" class="">it is defined in “{}” </blockquote><p id="11220209-ab2a-4fa0-9fe8-03855ab7cdb1" class="">syntax--</p><pre id="c8b3d7f4-5550-422e-8835-2806ae82ccd8" class="code"><code>d = {&#x27;name&#x27; : &#x27;tabish&#x27;, &#x27;age&#x27;: 21,&#x27;profession&#x27; : &#x27;student&#x27;}
for i in d:
	print(i+&quot; -- &quot;+str(d[i]))
</code></pre><figure class="block-color-gray_background callout" style="white-space:pre-wrap;display:flex" id="ec1a911a-da9c-4acb-9437-0d0b1cfff6d0"><div style="font-size:1.5em"><span class="icon">💡</span></div><div style="width:100%">=&gt; output
name -- tabish
age -- 21
profession -- student</div></figure><h3 id="764b5896-5279-4fe3-b62a-481ec66bde13" class=""><details open=""><summary>Dictionary Function</summary></details></h3><div class="indented"><pre id="dc19764d-05b7-45ab-979f-cad03ec4b329" class="code"><code>d = {&#x27;name&#x27; : &#x27;tabish&#x27;, &#x27;age&#x27;: 21,&#x27;profession&#x27; : &#x27;student&#x27;}</code></pre><p id="870c25ec-26cc-44e6-af97-5ad9e7226975" class=""><code>get()</code> -- gives the value when passes key (<code>d.get(&#x27;name&#x27;)</code>) =&gt; (<code>d[&#x27;name&#x27;]</code>) =&gt; tabish
<code>keys()</code> -- gives keys (<code>d.keys()</code>) (<code>for i in d.keys(): print(i)</code>)
<code>values()</code> -- gives values (<code>d.values()</code>) (same for loop as keys)
<code>items()</code> -- gives keys and values (<code>d.items()</code>) (<code>for i,j in d.items():print(i,j)</code>)<code>
del</code> -- deletes key and value when passes only key (<code>del d[&#x27;name&#x27;]</code>)
<code>pop()</code> -- deletes(key,value) and return(value) the key and value (<code>d.pop(&#x27;name&#x27;)</code>)
<code>dict()</code> -- creates a dictionary (<code>dict(name=&#x27;tabish&#x27;,age=21)</code>)  (<code>d[&#x27;age&#x27;] = 22</code>)
<code>update()</code> -- updates the value (<code>d.update({&#x27;age&#x27;:22})</code>)</p><p id="135392d0-cb1e-41ff-8dda-496b3360d7cc" class=""><code>d[&#x27;qualification&#x27;]</code> = &#x27;b.tech&#x27; — inserting new key and value in dictionary
<code>clear()</code> -- clear the whole dictionary (<code>d.clear()</code>)</p><hr id="90f2ee9b-7a6a-49c5-97a5-e12f2f5645fc"/></div><h3 id="3b61fa9d-a6f4-473b-aac4-54fd71c206b7" class=""><details open=""><summary>Nested Dictionary</summary></details></h3><div class="indented"><blockquote id="4fcb3a63-5804-4d4d-864d-e8579379a0a6" class="">collection of dictionaries in one single dictionary</blockquote><pre id="584ea935-2675-464e-8276-331a60809c52" class="code"><code>course = {
&#x27;php&#x27; : {&#x27;duration&#x27;: &#x27;2 months&#x27; , &#x27;fees&#x27; : 14000},
&#x27;python&#x27; : {&#x27;duration&#x27;: &#x27;2 months&#x27; , &#x27;fees&#x27; : 15500},
&#x27;java&#x27; : {&#x27;duration&#x27;: &#x27;2 months&#x27; , &#x27;fees&#x27; : 17000}
}
print(course[&#x27;php&#x27;])  
print(course[&#x27;php&#x27;][&#x27;fees&#x27;])</code></pre><figure class="block-color-gray_background callout" style="white-space:pre-wrap;display:flex" id="9d90ba62-00c7-42dc-966d-025a0721d93a"><div style="font-size:1.5em"><span class="icon">💡</span></div><div style="width:100%">=&gt; {&#x27;duration&#x27;: &#x27;2 months&#x27; , &#x27;fees&#x27; : 14000}   </div></figure><figure class="block-color-gray_background callout" style="white-space:pre-wrap;display:flex" id="7ecef2f2-5a5d-40e8-ad0f-31a44b8faedd"><div style="font-size:1.5em"><span class="icon">💡</span></div><div style="width:100%">=&gt;   14000</div></figure></div></div><hr id="5355b3e6-87e6-4d9a-84f5-99355fb8f73b"/><h2 id="58470a77-d01d-41c7-9991-1fce7233efc3" class=""><details open=""><summary>Tuple</summary></details></h2><div class="indented"><pre id="80034da6-e676-4a83-8934-4263b3e23cd1" class="code"><code>t = (20,30,40,50)
t[2] =&gt; 40</code></pre><p id="97cccff7-c9f5-44f9-a74b-d438c6830d0e" class=""><code>count()</code> -- counts the value in list (<code>t.count(50)</code>)
<code>max()</code> -- gives the maximum value in list (<code>max(t)</code>)   this also works for alphabets
<code>min()</code> -- gives the minimum value in list (<code>min(t)</code>)   this also works for alphabets
<code>index()</code> -- gives the index of passed value (<code>t.index(20)</code>)
<code>sum()</code> -- sum all elements in tuple (only works on int and float)(<code>sum(t)</code> =&gt; 140) (<code>sum(t,10)</code> =&gt; 150)
</p></div><hr id="e4449a3e-9509-4df0-ae91-ed3096d2894f"/><h2 id="fb54b186-3146-4181-9bc2-622a6d899451" class=""><details open=""><summary>Set</summary></details></h2><div class="indented"><blockquote id="11befde5-4700-4685-92bd-6ff30194a8b5" class="">Index doesn’t work on Set, Every value in set is unique, it is defined in ‘{}’</blockquote><blockquote id="e517767c-69fc-466d-8c5c-4f4e964320cc" class="">set can be randomly printed</blockquote><pre id="6ddd6b04-587a-452a-a27e-5117b6489590" class="code"><code>s = {10,20,30}
for i in s:
	print(i)</code></pre><pre id="2e4db929-348e-4ffe-a3ac-dc5cb475be24" class="code"><code>=&gt;
10
20
30</code></pre><p id="c4ce7e97-98b1-4b34-bef1-9bf945883950" class=""><code>set()</code> -- converts a list to set (<code>set([10,20,30])</code>)
<code>add()</code> -- adds new value to set(<code>s.add(40)</code>)
<code>pop()</code> -- delete and return random value(<code>s.pop()</code>)
<code>remove() </code>-- takes value and delete it (<code>s.remove(20)</code>)
<code>discard() </code>-- same as remove (<code>s.dicard(20)</code>)
<code>clear() </code>-- deletes everything (<code>s.clear()</code>)
<code>update() </code>-- adds list to set (<code>s.update(l) </code>=&gt; {10,20,30,40,50})
</p></div><hr id="d23a5fe7-d33b-43b5-8515-a98d103db5ca"/><h2 id="52631e7b-42f7-4ec5-8511-590b0efa8fa8" class=""><details open=""><summary>Conditional Statements</summary></details></h2><div class="indented"><ol type="1" id="f128f14b-5687-4b22-bc11-39be7fa54329" class="numbered-list" start="1"><li><strong>if statement</strong></li></ol><ol type="1" id="3b0b46dc-585c-46d5-85e0-2eb3acc0a918" class="numbered-list" start="2"><li><strong>if else statement</strong></li></ol><ol type="1" id="6f64c05b-d4a7-470b-acd8-e94ef30f804d" class="numbered-list" start="3"><li><strong>if elif else statement</strong></li></ol><pre id="17d8fcd0-a5ea-4d86-b5ab-186287589e97" class="code"><code>if a==10:
	print(&#x27;a is ten&#x27;)
elif a == 20:
	print(&#x27;a is twenty&#x27;)
else :
	print (&#x27;a is not ten,twenty&#x27;)</code></pre></div><hr id="5605cb95-4cfc-4386-b032-2776633bf82e"/><h2 id="67200cec-25be-435e-a013-70f5f6b5d3c2" class=""><details open=""><summary><strong>Range</strong></summary></details></h2><div class="indented"><ul id="475a8458-9e5f-4345-afa6-12d541689a87" class="toggle"><li><details open=""><summary><code>range(5)</code></summary><p id="d21dc0b0-0769-4843-bd5c-05331ef348ca" class="">start = 0 -- default
conditon &lt; 5
increment = 1 -- default</p></details></li></ul><ul id="7af4183c-3857-49ce-b0b0-f99e6d4ea3ae" class="toggle"><li><details open=""><summary><code>range(5,7)</code></summary><p id="c2842d60-c9e2-4679-8be6-bef44117b528" class="">start = 5
conditon &lt; 7
increment = 1 -- default</p></details></li></ul><ul id="e1d2006f-ad82-469d-be80-71f10826a269" class="toggle"><li><details open=""><summary><code>range(1,15,3)</code></summary><p id="a2247f2e-29bb-4c56-aa34-2d7408185b8e" class="">start = 1
conditon &lt; 44
increment = 3</p></details></li></ul><ul id="3c0df9bd-a0e5-46ad-bdee-3b936e95ad5e" class="toggle"><li><details open=""><summary><code>range(10,0,-1)</code> </summary><p id="22e222e4-68d2-483d-b0a0-b3fb37301b44" class="">this is a reverse function
start = 10
condition &gt; 0
decrement = -1</p></details></li></ul></div><hr id="b823f3a4-2143-4dce-989b-b6d33ac203d6"/><h2 id="5206596d-2ba1-4ca8-a108-e8530b8d8d9c" class=""><details open=""><summary><strong>Loops</strong></summary></details></h2><div class="indented"><ul id="3c64719a-939c-4e9f-bc72-7df363fd9089" class="toggle"><li><details open=""><summary><strong>for</strong> <strong>loop</strong></summary><pre id="ea3f0cbd-b801-4267-a81f-08c7a775743d" class="code"><code>for i in range(5);
	print(i, &#x27;hi&#x27;)</code></pre></details></li></ul><ul id="80a76f84-5700-4024-bf59-a50e6c655e41" class="toggle"><li><details open=""><summary><strong>while loop</strong></summary><pre id="463432e5-621f-43a1-a46c-b7f89fa9981b" class="code"><code>i = 1
while i &lt;= 10:
print(i)
i += 1</code></pre><figure class="block-color-gray_background callout" style="white-space:pre-wrap;display:flex" id="3d7607ac-8c10-4d7b-8081-8f9c0f6de303"><div style="font-size:1.5em"><span class="icon">💡</span></div><div style="width:100%">after while loop the value of <code>i</code> will be 11</div></figure></details></li></ul></div><hr id="24a53daf-15e2-40d4-81dc-c39162ba1bea"/><h2 id="62080531-9fcb-431a-b10b-249844256b4e" class=""><details open=""><summary>Functions</summary></details></h2><div class="indented"><blockquote id="d57826aa-fc8b-4430-9195-d07314c30d8a" class="">A function is a block of statements which can be used repetitively in a program. It saves the time of a developer. In python concept of function is same as in other language. you can pass data, known as parameters or arguments into a function.</blockquote><figure class="block-color-gray_background callout" style="white-space:pre-wrap;display:flex" id="e2996280-90e5-4664-b589-cbd4ad8032bd"><div style="font-size:1.5em"><span class="icon">💡</span></div><div style="width:100%">creating a function is defined using the &quot;def&quot; keyword</div></figure><p id="7567e5db-0abd-4407-94a2-c6a26cd4547f" class=""><strong>Input</strong>
<code>input(&#x27;Enter the value:- &#x27;)</code></p><p id="6aa82008-7ac5-4469-a439-a37c8fc6185c" class="">(put input function in a variable to safe the input value in the same variable)</p><hr id="cd329c9a-6855-4284-a225-fac320540ec6"/><ol type="1" id="856ea533-eac5-41a2-9c20-e7c90828a422" class="numbered-list" start="1"><li><strong>Simple function</strong></li></ol><ol type="1" id="d4cc258a-8574-44d5-994c-343cc3ede715" class="numbered-list" start="2"><li><strong>Function with arguments</strong></li></ol><ol type="1" id="3472f29e-fdf4-4d0b-a8cd-ec00a3724795" class="numbered-list" start="3"><li><strong>Return type</strong></li></ol><h3 id="380b97ee-007b-4d47-9e10-94d6ecc16854" class=""><details open=""><summary>simple function</summary></details></h3><div class="indented"><pre id="3c99876b-c81c-4a49-afb8-21f61519466e" class="code"><code>def func():
	print(&#x27;this is a simple function &#x27;)

func()</code></pre></div><h3 id="018743b9-9a4a-4a72-902d-39d4b512d49c" class=""><details open=""><summary>function with argument</summary></details></h3><div class="indented"><pre id="76823911-55c7-4ff8-a16b-eb2a6d8891a2" class="code"><code>def sumdata(i,j=5):
	print(i+j)

sumdata(10) 
sumdata(10,20)</code></pre><figure class="block-color-gray_background callout" style="white-space:pre-wrap;display:flex" id="76412263-d4db-4ca4-85b6-1bfcd697832e"><div style="font-size:1.5em"><span class="icon">💡</span></div><div style="width:100%">=&gt; 15</div></figure></div><h3 id="bff9bafb-8bbe-440c-834c-254e27deb997" class=""><details open=""><summary>return type function</summary></details></h3><div class="indented"><pre id="811e06c6-9c55-49aa-9d6b-e22beead9df5" class="code"><code>def subtractData(a,b):
	return a-b

s = subtractData(40,25)
print(s)</code></pre></div></div><hr id="e1cd89db-7468-483e-87b0-773c32acee4f"/><div><h1 id="b849f47c-585d-4e0e-9a81-980733d7e9ec" class=""><details open=""><summary><mark class="highlight-teal">Modules</mark></summary></details></h1><div class="indented"><blockquote id="75d91eaf-de58-4f52-8a37-9ebbb9143f7b" class="">you can import modules</blockquote><pre id="0e9d549c-12f9-41a6-a774-0b56b5d39b18" class="code"><code>import module1 as m //giving alias as m 
from module1 import sum // importing only a function from a module 
from module1 import * //importing everything from a module</code></pre><h3 id="64173097-4196-4c2b-9136-e81800bc8fe8" class=""><details open=""><summary>Math Module</summary></details></h3><div class="indented"><pre id="b6a5b0c9-bc51-4bb2-b47e-6d94c993eb76" class="code"><code>import math as m</code></pre><p id="d358270e-3e01-497b-b599-2debb35ab945" class=""><code>ceil()</code> = changes float value to int by adding in it (10.5 =&gt; 11)
<code>fabs() </code>= changes negative value to positive
<code>factorial() </code>= gives the factorial of the given value, value shouldn&#x27;t be negative or non-integer (3 =&gt; 1*2*3 =&gt; 6)
<code>floor() </code>= changes float value to int by subtarcting in it (10.5 =&gt; 10)
<code>fsum() </code>= can get list &amp; tuple as a parameter to add its element and return it
<code>sqrt() </code>= returns the square root</p></div><h3 id="a79cb138-5dec-4003-9382-7ea2bc69f19b" class=""><details open=""><summary>Random Module</summary></details></h3><div class="indented"><pre id="1860452d-a88d-403c-8f66-1e46304fa780" class="code"><code>import random as r</code></pre><p id="b7a541b8-b93e-4c1d-832d-6a695431b69e" class=""><code>randint() </code>=&gt; takes 2 arguments and gives the random value from between them and both parameter are included
<code>randrange() </code>=&gt; same as <code>randint()</code> but second argument is not included
<code>choice() </code>=&gt; return a random element from a list
<code>random() </code>=&gt; retrun random float between  0 to 1
<code>shuffle() </code>=&gt; takes a sequence and return the it in random order
<code>unifrom() </code>=&gt; returns a random float between 2 parameters</p></div><h3 id="3aeb78eb-8545-4d74-b37c-960585eae6f1" class=""><details open=""><summary>Date and time module</summary></details></h3><div class="indented"><pre id="93c43119-390f-41c0-b6a0-f0c709cc487e" class="code"><code>import datetime as dt
now = dt.datetime.now()</code></pre><p id="9b6807b4-777f-4c76-97c5-eeed8d53a387" class=""><code>print(now)</code> =&gt; gives current date and time
<code>datetime(2022,8,16)</code> =&gt; gives parameter in date and time format</p><pre id="2878ea3e-208d-42fa-b555-05924fa122e1" class="code"><code>print(now.strftime()) =&gt; shows everything of now but takes arguments as
        %b = Dec
        %B = December
        %m = 12 (month)
        %y = 21 (year)
        %Y = 2021 (year)
        %H = 17 (hour in 24)
        %I = 7 (hour in 12)
        %p = PM (AM/PM)
        %M = 54 (minutes)
</code></pre></div><h3 id="b3231b7d-7010-4a7d-b996-199abb02c437" class=""><details open=""><summary>Pickle module</summary></details></h3><div class="indented"><blockquote id="cef0aca7-2c40-4176-bb8d-5e746436baf4" class="">This module implements a fundamental, but powerful algorithm for serializing and DE serializing a python object structure</blockquote><pre id="5c7fad27-91f3-4b0d-ae69-aa5747dc8c0e" class="code"><code>import pickle as p</code></pre><p id="180ec0b1-b3c2-4c6b-9052-aa6b7db65e39" class=""><code>dump()</code> -- to serialize an object hierarchy
<code>load()</code> -- to de-serialize a data stream
<code>wb</code> -- write binary
<code>rb</code> -- read binary</p></div></div></div><hr id="0ebe7d3d-d585-49e4-a083-cc9604751344"/><h2 id="71265737-fb46-4458-ab92-13ac9c6ff9f7" class=""><details open=""><summary>OOPs (Object Oriented Programming) </summary></details></h2><div class="indented"><pre id="0e92c6a4-753e-4d66-a8c9-fec3764e2563" class="code"><code>class DemoClass :
	a =10
	def sumValue(self) :
	  print(20+30)

demo = DemoClass()
demo1 = DemoClass()

print(demo.a)
print(demo1.a)
demo.sumValue()</code></pre><figure class="block-color-gray_background callout" style="white-space:pre-wrap;display:flex" id="cee65789-0eac-492d-8986-37c37654aa07"><div style="font-size:1.5em"><span class="icon">💡</span></div><div style="width:100%"><strong>Method</strong> -- if function is define in class it is known as method and you have to call it
when making a method you have to pass any one argument (self) and if you are using class variable then you have to call self to use it
<strong>Constructor </strong>-- same as method but you don&#x27;t call it</div></figure><pre id="fc24db63-5359-4578-822d-e0904c233f8c" class="code"><code>class Dummy:
	a=10
	def init(self):
		print(&#x27;This is a Constructor&#x27;)

	def showValue(self):
    print(self.a)
    print(self.a*self.a)

	def show(self,a,b):
    print(&#x27;this is tabish shaikh &#x27;,a,b)

obj = Dummy()
obj.showValue()
obj.show(5,7)</code></pre><h3 id="1ee8a1c0-2dea-4342-9d04-ce27f25eb90d" class=""><details open=""><summary><strong>Inheritance</strong></summary></details></h3><div class="indented"><ul id="579dec92-9d15-46ea-937b-b3db4b6e416b" class="bulleted-list"><li style="list-style-type:disc"><strong>Single level</strong></li></ul><pre id="081fedec-87d4-4822-b0d1-4207f3ac20e7" class="code"><code>class A:
	def displayA(self):
		print(&#x27;Tabish A&#x27;)

class B(A):                            \\passing class as a argument to another class
	def displayB(self):
		print(&#x27;Tabish B&#x27;)

obj=B()                                \\ object b can use class A&#x27;s methods
obj.displayB()
obj.displayA()</code></pre><ul id="168a6fdf-ecf4-4c4f-80bf-977b50744693" class="bulleted-list"><li style="list-style-type:disc"><strong>Multi level</strong></li></ul><pre id="40c846eb-b04c-46d4-98fb-e1872b166ce9" class="code"><code>class A:
	def displayA(self):
		print(&#x27;Tabish A&#x27;)

class B(A):                     \\passing class as a argument to another class
	def displayB(self):
		print(&#x27;Tabish B&#x27;)

class C(B):                     \\passing class as a argument to another class
	def displayC(self):
		print(&#x27;Tabish C&#x27;)

obj=C()                         \\ object of C can use class B&#x27;s as well as A&#x27;s methods bcoz its passed from c to b to a
obj.displayC()
obj.displayB()
obj.displayA()</code></pre><ul id="a63fbf45-9210-4bce-978b-370c9e2f0e30" class="bulleted-list"><li style="list-style-type:disc"><strong>Multiple level</strong></li></ul><pre id="7b38ac37-6d8e-4009-aecd-c7e61e9c22fc" class="code"><code>class A:
	def displayA(self):
		print(&#x27;Tabish A&#x27;)

class B:
	def displayB(self):
		print(&#x27;Tabish B&#x27;)

class C(A,B):                \\passing class as a argument to another class
	def displayC(self):
		print(&#x27;Tabish C&#x27;)

obj=C()                      \\ obj of C can use class B&#x27;s and A&#x27;s methods as they were passed in C class but object B can&#x27;t use A&#x27;s , nor A&#x27;s can&#x27;t uses B&#x27;s
obj.displayC()
obj.displayB()
obj.displayA()</code></pre></div><h3 id="82541084-da20-42fb-a294-47dceab44457" class=""><details open=""><summary><strong>Encapsulation</strong></summary></details></h3><div class="indented"><blockquote id="240a9afd-65a9-4ca9-a4cb-da37cc962795" class="">An objects variable should not always be directly accessible
the method can check the correct values are set, if not then return an error</blockquote><pre id="343c3c33-3bd2-4307-b528-95edc49ebd22" class="code"><code>class Student:
	def init (self):
		self.__name=&quot;&quot;
	def getname(self):
		return self.__name
	def setname(self,name):
		self.__name = name

obj = Student()
obj.setname(&quot;Tabish&quot;)
name = obj.getname()
print(name)</code></pre><hr id="693fa600-da11-414c-b950-051fd86e861b"/><pre id="179e1427-3d22-465d-a32a-c408ace73295" class="code"><code>class Student:
	__name = &quot;shaikh&quot; #the double underscore means private or encapsulation. this can&#x27;t be use in object until constructor ask
	def init(self):
		print(self.__name)
		self.__displayInfo()
	def __displayInfo(self):
		print(&quot;this is private method&quot;)

obj=Student()</code></pre><p id="13fc7a6e-0ada-4804-bc3d-d4f847d1d347" class="">
</p></div><h3 id="10be4ee8-dace-4a92-af1a-687b107aeef0" class=""><details open=""><summary><strong>Polymorphism</strong></summary></details></h3><div class="indented"><blockquote id="68be8ebb-80e3-4762-93b5-3515a9fc3a9c" class="">it means same function name (but different signatures) being uses for diff. types =&gt; <code>len([12,32,2])</code>=&gt; <code>len(&#x27;shaikh)</code></blockquote><ul id="1e954ed4-f2e2-46d7-b725-20c6d6430b16" class="toggle"><li><details open=""><summary><strong>Overloading</strong></summary><blockquote id="f034530a-1dac-44c1-908d-912156fb296e" class=""> same method different type of parameter</blockquote><pre id="c21b5a21-d82e-488e-b7df-9727fd869da3" class="code"><code>class sh:
	def dInfo(self,name=&#x27;&#x27;):
		print(&#x27;welcome to terminal&#x27;,name)

obj = sh()
obj.dInfo()
obj.dInfo(&#x27;tabish&#x27;)</code></pre><pre id="99d40a00-e233-4dc5-a7f7-2d8872f798d2" class="code"><code># another example
class Area:
	def find_area(self,x=None,y=None):
		if x != None and y != None:
			print(&#x27;The Area of Rectangle is &#x27;, xy)
		elif x != None:
			print(&#x27;The Area of Square is &#x27;, xx)
		else:
			print(&#x27;Nothing to find&#x27;)

obj=Area()
obj.find_area()
obj.find_area(10)
obj.find_area(10,20)</code></pre></details></li></ul><ul id="7460b039-2300-4875-9f18-27869a3a9e1e" class="toggle"><li><details open=""><summary><strong>Overriding</strong></summary><blockquote id="2329ebcc-7f31-4513-8a7a-99ccbb9f3381" class=""> to use the same name method from parent class</blockquote><pre id="11c70175-b52b-4e76-8dca-632d3b0fd2cb" class="code"><code>class sh:
	def dInfo(self):
		print(&#x27;welcome to SH&#x27;)

class jh(sh):
	def dInfo(self):
		super().dInfo() #to use the same name method from parent class use super
		print(&#x27;welcome to JH&#x27;)

obj = jh()
obj.dInfo()</code></pre></details></li></ul></div></div><hr id="5d88ce9a-d6d7-436e-9c1f-1a4b3558d246"/><h2 id="d7dd3af6-a00c-4fce-b42b-5b3795fc852c" class=""><details open=""><summary>Error and Built-in Exception</summary></details></h2><div class="indented"><ol type="1" id="d0a58a05-ad82-4b8f-a1ca-ae66c340d7e7" class="numbered-list" start="1"><li><strong>Syntax</strong> <strong>Error</strong></li></ol><ol type="1" id="d6b925c0-4158-476e-9632-99ce5c8d2cf8" class="numbered-list" start="2"><li><strong>Logical error (Exception)</strong><ol type="a" id="1eaa492b-bf97-45c5-9f8b-a710774d7210" class="numbered-list" start="1"><li>Zero Division Error (<code>a=0</code> -- <code>print(a/0)</code>)</li></ol><ol type="a" id="eead179f-4d3c-4236-aafa-3a9c18c18a74" class="numbered-list" start="2"><li>Name Error (<code>print(b)</code>)</li></ol><ol type="a" id="1f7eec6e-5f7b-4d9f-a9a4-8a9184cb35ce" class="numbered-list" start="3"><li>Type Error (<code>print(&#x27;10&#x27; + 10)</code>)</li></ol><ol type="a" id="22b1f530-77de-4f3e-873a-b9e8f38429ea" class="numbered-list" start="4"><li>Value Error (<code>a=int(input(enter))</code> -- <code>a=&#x27;hello&#x27;</code>)</li></ol><ol type="a" id="e3c417a5-0166-4599-8b0f-60422eec9837" class="numbered-list" start="5"><li>Index Error (<code>l=[1,2,3,4]</code> -- <code>print(l[6])</code>)</li></ol><ol type="a" id="bdf1ccd4-f2da-4bba-a38d-9b536148f982" class="numbered-list" start="6"><li>Key Error (<code>a={&#x27;name&#x27;:&#x27;error&#x27;,&#x27;fee&#x27;:7000}</code> -- <code>print(a[&#x27;fees&#x27;])</code>)</li></ol><ol type="a" id="9c165159-5f61-4bc7-99c2-aa0d13f85082" class="numbered-list" start="7"><li>Module Not Found Error (<code><a href="http://cal.py/">cal.py</a></code> -- <code>import cals</code>)</li></ol><ol type="a" id="1babc0b4-2fbc-4391-8ab0-048ec8b68cc9" class="numbered-list" start="8"><li>Import Error (<code>sum()</code> -- <code>from cal import sum1</code>)</li></ol></li></ol><pre id="0276b4ce-f814-445e-bcce-9fee64ace49f" class="code"><code>num1 = input(&#x27;enter num1&#x27;)
num2 = input(&#x27;enter num2&#x27;)

try:
	print(&#x27;num1 + num2 =&gt; &#x27;,num1+num2)
except Exception as e:
	print(e)

print(&#x27;done&#x27;)</code></pre></div><hr id="4af49fc0-20c7-4a9c-b85e-0b51572ce4dc"/><h2 id="a6c7a789-c34c-4c71-bc05-32e2956daeaf" class=""><details open=""><summary>SQLite</summary></details></h2><div class="indented"><blockquote id="ee6f15cf-ab13-41c1-b149-e2eae2ef4127" class="">extension =&gt; .db</blockquote><pre id="3c837057-8989-4f5c-b1c4-f32478c42a14" class="code"><code>import sqlite3      #importing sqlite module
con = sqlite3.connect(&quot;sqlite1.db&quot;)         #connecting OR connecting and creating database file in same path as py file
con.execute(&#x27;create table tabish&#x27;)      # creating table and passing column names and data structure that they will carry
con.close()     #closing file</code></pre></div><hr id="4bfd2d7f-3c43-4c17-adaf-f27de190677b"/><hr id="de41efc4-80b9-4031-9d92-3f975093577b"/><hr id="e18e2872-c105-4142-96da-447860a9c79f"/><hr id="5b4081c6-322b-4a9d-b473-95b591ab2bd7"/><pre id="f2807dd5-e699-4daa-ae5e-1dc680ba4a7c" class="code"><code>this file is created by Md Tabish Shaikh for learning purpose.</code></pre><p id="b89043ce-a2bc-42f5-b838-84562945bf24" class="">
</p></div></article></body></html>
