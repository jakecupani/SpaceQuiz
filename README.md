# SpaceQuiz - INFM 603 Group Project
https://spacequiz603.herokuapp.com/

## Background

National Aeronautics and Space Administration (NASA) is the United States federal agency responsible for scientific and technological achievements in human spaceflight, aeronautics, space science, and space applications. NASA’s Science, Technology, Engineering, and Mathematics (STEM) Engagement Program strives to increase K-12 involvement in NASA projects, enhance higher education, support underrepresented communities, strengthen online education, and boost NASA's contribution to informal education.

Inspired by NASA’s mission and the goals of its STEM Engagement Program, graduate students in the University of Maryland College Park’s College of Information Studies (iSchool) created a proposed website for their INFM 603, Information Technology and Organizational Context, group project.

The group of five graduate students played the role of a hypothetical web development and consulting firm and project team that would be contracted by NASA to create a website related to its STEM Engagement Program. The group of five graduate students were not contracted by NASA, did not create any products for NASA, and did not perform any services for NASA whatsoever.

The proposed website the graduate students created would hypothetically be used to further the goals of the NASA STEM Engagement Program by increasing K-12 involvement in NASA projects, strengthening online education, and boosting NASA’s contribution to informal education.

The proposed website would provide elementary and middle school students with educational information on a variety of STEM topics related to NASA’s Moon to Mars exploration plans. After studying this information, students would be able to demonstrate and measure their understanding of these topics. Specifically, students could answer a set of quiz questions about NASA, including its Artemis mission to send the first woman and next man to the Moon by 2024 and preparation to send astronauts to Mars.

## Website

The proposed website consists of three web pages:
 - Home - A page welcoming students before they preceding throughout the site; 

 ![Home Page](./nasaswyk/nasaswyk/static/assets/HomePage.jpg)

 - Quizzes - A page where student select NASA-related STEM topics to demonstrate and measure their understanding;

 ![Quizzes Page](./nasaswyk/nasaswyk/static/assets/QuizzesPage.jpg)

 - Quiz Results - Provides students a percentage score based on the number of quiz questions they answered correctly and provides explanations for quiz questions they did not answer correctly; and

 ![Quiz Results Page](./nasaswyk/nasaswyk/static/assets/QuizResultsPage.jpg)

 - About - A page providing information for students, teachers, and parents on the site's purpose.

 ![About Page](./nasaswyk/nasaswyk/static/assets/AboutPage.jpg)    

## Planning and Design

The project team met on a weekly basis via Zoom to discuss the website. Project team members also met on an ad-hoc basis via Zoom or Google Meet to discuss specific tasks. The project team communicated outside meetings using GroupMe.

The project team used Google Drive and Trello boards to manage documents, as well as the planning and design of the website. 

The project team stored its documentation on Google Drive. 

![Google Drive](./nasaswyk/nasaswyk/static/assets/GoogleDrive.jpg)

The project team used Trello for project planning.

![Trello for Project Management](./nasaswyk/nasaswyk/static/assets/TrelloforProjectManagement.jpg)

The project team wrote users stories for students, teachers, parents, and others to identify and develop website requirements and tracked the backlog, user stories, and sprints using Trello.

![Trello for User Stories](./nasaswyk/nasaswyk/static/assets/TrelloforUserStories.jpg)

The project team developed wireframes of the user interface for the main pages of the website using Figma. 

![Figma for Wireframes](./nasaswyk/nasaswyk/static/assets/FigmaforWireframes.jpg)

The team also developed wireframes for some of the major epics in the project’s backlog using Figma. 

![Figma for Backlog Wireframes](./nasaswyk/nasaswyk/static/assets/FigmaforBacklogWireframes.jpg)

The project team drafted an Entity-Relationship Diagram (ERD) to define the website’s conceptual data model for the database of quiz questions and answers. This ERD was created using Figma.

![Figma for Entity Relationship Diagram](./nasaswyk/nasaswyk/static/assets/FigmaforEntityRelationshipDiagram.jpg)

## Implementation

The website was created to be web browser agnostic. The website was also created for use on both desktop/laptop computers and hand-held devices and considers the resolution and interactivity of its display. Lastly, the website was created for use on all operating systems.

The website consists of HTML code for site foundation and Bootstrap for site stylings and design. The site also consists of Python code used in the Django web framework to create the Home, Quizzes, Quiz Results, and About pages. For quiz questions, an SQL data store was used. Python and Django were used to create quizzes based on the user selection of topic(s) and difficulty level. The site was deployed using Heroku.

## Testing

The project team tested website functionality on the Chrome, Edge, Firefox, and Safari web browsers.

The project team used the Google Chrome Lighthouse audit tool to assess various performance, accessibility, best practices, and search engine optimization (SEO) factors by giving a score for each factor being assessed. This tool assessed mobile and desktop usability and responsiveness for the Home, Quizzes, Quiz Results, and About Pages. This tool was used to detect inefficiencies and mistakes as well as areas to improve our HTML code and other assets. The project team also used the Google Chrome Developer Tools console to debug errors in the HTML code.

### Google Chrome Lighthouse Testing Results

#### Desktop Audit Testing Results Example

![Google Chrome Lighthouse Desktop Audit Testing Results](./nasaswyk/nasaswyk/static/assets/GoogleChromeLighthouseHerokuDesktop.jpg)

#### Mobile Audit Testing Results Example

![Google Chrome Lighthouse Mobile Audit Testing Results](./nasaswyk/nasaswyk/static/assets/GoogleChromeLighthouseHerokuMobile.jpg)

The project team also used manual tests to check the functionalities of the website and its underlying database based on the actions of website users. For example, the project team performed tests to assess whether:
 - Topic buttons loaded all appropriate quizzes and no others.
 - Difficulty buttons loaded all appropriate quizzes and no others.
 - Inappropriate use (“mashing”) of buttons did not break site functionality.

 The group tracked testing and bugs using Trello.

![Trello for Testing and BugTracking](./nasaswyk/nasaswyk/static/assets/TrelloforTestingandBugTracking.jpg)

## Backlog and Backlogged Items

The project team created a backlog of future functionality for the website. These items were identified and discussed during different stages of the project. These items were documented in meeting minutes on the Google Drive, on one of the Trello boards, as well as on our Figma site. These backlogged items can be added to future releases of the site to improve its content and functionality. Items in the backlog included:

 - Additional information, hyperlinks, videos, and/or pages that students can read and watch to learn more about a specific topic;
 - Pages where students can receive instructions for individual learning activities, such as observing and identifying the lunar cycle;
 - Site functionality that would randomize the selection of quiz questions for topics;
 - Pages where students can type and submit short answers responses to questions related to individual learning activities; 
 - A page where students can type and submit questions to their teacher; 
 - Site functionality to capture and send quiz scores via email to teachers and/or parents for their review; and
 - A credential and portal system for students, teachers, parents, and others that allows them to view quiz scores and other class information.

#### Trello Backlogged Item Example

![Trello Backlogged Item Example](./nasaswyk/nasaswyk/static/assets/TrelloforBacklog.jpg)

## Challenges and Lessons Learned

The project team learned from challenges they encountered while working on the website.

The project team considered the identification and development of website requirements as a challenge. The project team was unable to discuss and work with students, teachers, parents, and those with subject matter expertise in NASA and STEM topics to obtain their input and feedback on the site content and functionality. As a result, the project team learned the importance of stakeholder engagement in website development. To overcome this challenge, the project team recommends creating an advisory board of users to obtain input and feedback on site content and functionality. After working with this advisory board, the project team would revisit and revise any user stories, requirements, site content and functionality for future releases.

The project team considered its technical proficiency in web development applications as another challenge. While the project team was able to successfully implement, test, and deploy the website, it experienced difficulty learning how to use Bootstrap, Django, GitHub, and Heroku. The project team acknowledged that these applications have steep learning curves which require additional and sustained use to master them. To overcome this challenge, the project team recommends engaging in future experiential learning opportunities to improve their proficiency in these applications. By doing so, the project team members will be able to master these applications as well as develop practical solutions for complex problems.

## References

The project team referred to and used subject matter, image, and technical resources for the website. These resources were used to assist in the planning, design, implementation, and testing of the site. 

The project team referred to and used information from the following websites, documents, and videos for subject matter related to NASA:

 - [NASA History Overview](https://www.nasa.gov/content/nasa-history-overview)
 - [NASA STEM Engagement Website](https://www.nasa.gov/stem/about.html)
 - [NASA Strategy for STEM Engagement Document](https://www.nasa.gov/sites/default/files/atoms/files/nasa-strategy-for-stem-2020-23-508.pdf)  
 - [NASA We Are Going Video](https://youtu.be/vl6jn-DdafM) 
 - [NASA Prepares to Explore Moon: Spacesuits, Tools Video](https://moon.nasa.gov/resources/410/nasa-prepares-to-explore-the-moon-spacesuits-and-tools/)
 - [NASA Exploration Mission - 1: Pushing Farther Into Deep Space Video](https://youtu.be/XcPtQYalkcs)
 - [NASA Moon to Mars Website](https://www.nasa.gov/topics/moon-to-mars)
 - [NASA Artemis Program Website](https://www.nasa.gov/specials/artemis/)
 - [NASA NASA Knows! for Students 5-8 Website](https://www.nasa.gov/audience/forstudents/5-8/features/nasa-knows/index.html)

The project team used images from the following sources:

 - [NASA's Unsplash Webpage](https://unsplash.com/@nasa)
 - [NASA Image Gallery Webpage](https://www.nasa.gov/multimedia/imagegallery/index.html)
 - [World Vector Logo](https://worldvectorlogo.com/logo/galaxy-4)
 - [Freepik](https://www.freepik.com/free-vector/space-seamless-pattern_1537681.htm)
 
 The project team referred to and used information from the following technical sources:
 - [Bootstrap](https://getbootstrap.com/docs/4.4/getting-started/introduction/) and [w3schools](https://www.w3schools.com/css/default.asp)  for site stylings and design
 - [Django](https://docs.djangoproject.com/en/3.1/intro/tutorial01/) for web development 
 
## Documents Appendix

Go to INFM603/documents/Documents Appendix for Group Project Report/ for documents related to project management, specifications, software testing, and the final project presentation. 
