# S.K.A.T.E Trick generator


<h2>Contents</h2>
<ul>
  <li>
    
   [The Brief](#the-brief)
    
  </li>
  <ul>
    <li>
  
   [My application](#my-application)
  
  </li>
 </ul>
 <li>
  
  [Architecture](#architecture)
  
  </li>
  <ul>
  <li>
    
   [ED](#entity-diagrams)
   
   </li>
   
   </ul>
   <li>
  
  [CI pipeline](#ci-pipeline)
  
  </li>
  <li>
  
  [Risk Assessment](#risk-assessment)
  
  </li>
  <li>
  
  [User Stories](#user-stories)
  
  </li>
  <li>
  
  [Testing](#testing)
  
  </li>
  <li>
  
  [Known Issues](#known-issues)
  
  </li>
  <li>
  
  [Future Improvements](#future-improvements)
  
  </li>
  <li>
  
  [Authors](#authors)
  
  </li>
 
 </ul>  
<h2>The brief</h2> 
<p1>To create an application that creates 'Objects' that is made from a set of predefined rules. This will have to be accopmplished using the technologies and methodologies taught. </p1>
<br>
<h3>My application</h3>
<p1>My project is an application that generates a random skate trick and combining it with a stance. The steeze is dependent on what the stance and trick is.</p1>
<br>
<h2>Architecture</h2>

![diagram](https://i.imgur.com/dXKgatX.png)
<ul>
  <li>1_server: Sends out a request to 4_SKATE, to return the full trick, that is diplayed on a HTML page.< /li>
   <li>2_stance: This recieves a request from 4_SKATE, asking for a stance. A random number is generated which determines which ID is chose out of the stance table </li>
  <li>3_trick: This recieves a request from 4_SKATE, asking for a trick. A random number is generated which determines which ID is chose out of the trick table</li>
    <li>4_SKATE: This recieves a request from 1_server, so it then send out requests to 2_stance and 3_trick, to get the stance and trick. Once they have been retrieved, the steeze is then calculated, dependent of the stance and trick. Once this is done, these value are stored in a dict and jsonify'd.</li>
    <li>NGINX: Is used as a reverse proxy, this is so the use does not have direct access to VM's</li>
    <li>SQL DB: This has preset list within the stance and trick tables, these are queried and information is sent back to the relevant place</li>
</ul>
<h3>Entity Diagrams</h3>

![ed](https://i.imgur.com/EDcIuMl.png)

<h3>CI-pipeline</h2>

![ci](https://i.imgur.com/SHAnhaC.png)

<p1>The picture is below is the continuous integration pipeline. This allows for rapid and efficient development to deployment. Using webhooks, once the user pushes code to the master branch, the code is tested, if it pasts the tests, then ansible is installed on the machine and docker starts to build the images. This allows for there to me no down time during deployment.</p1>

<h3>Risk Assessment</h3>

![risk](https://i.imgur.com/MJJ2tm5.png)

<h2>User Stories</h2>

![user](https://i.imgur.com/SnzC0WD.png)

<p1>To track the progress of the project and layout what was needed, Githubs project tracker was used to do this. I linked issues to certain pull-requests therefore slightly automating the kanban board.</p1>
<p1>The board has several collumns, this allowed to keep tabs on the progress.</p1>
<ul>
  <li><i>To do</i>: This showed what was still needed to be completed</li>
  <li><i>In progress</i>: This shows what is currently being worked on</li>
  <li><i>Completed</i>: This shows all the issues that have been completed </li>
  <li><i>User Stories</i>: This shows all the user stories </li>
</ul>


<h2>Testing</h2>

<h3>Unit Testing</h3>

![unit1](https://i.imgur.com/nL9RHXm.png)

![unit2](https://i.imgur.com/GZCBB9e.png)

![unit3](https://i.imgur.com/fHBOMeF.png)

![unit4](https://i.imgur.com/MiSAehd.png)

![unit4a](https://i.imgur.com/X6Ks8oH.png)

<p>High coverage was produced accross all services, unfortunately when implementing new features, I was un able to get high coverage of 4_SKATE. Testing is fully automated, so whenever someone pushes code to master branch, it is tested.</p>

<h2>Known Issues</h2>
<ul>
  <li>Due to the limited resources of GCP, after all images are uploaded and updated, sometimes it will revert to the old code, but only for a few seconds.</li>
</ul>

<h2>Future improvements</h2>
<ul>
  <li>Allow for the user to store their trick< /li>
   <li>Higher coverage on 4_SKATE</li>
  <li>Improve the front end, and make it more visually appealing</li>
</ul>

<h2>Authors</h2>
<p1>James Jeffrey</p1>


