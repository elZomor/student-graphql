[![LinkedIn][linkedin-shield]][linkedin-url]

<br />
<div>

<h3 align="center">Student-Courses backend with GraphQL</h3>

  <p align="center">
    Student with mobiles and courses project with GraphQL APIs
</div>

<!-- ABOUT THE PROJECT -->
## About The Project
Using Django framework and GraphQL, I have built a project where we have a table of students, also a table of 
mobiles associated with students (Many to One). Also a table of courses with a many-to-many relationship with the
 students  
Also JWT authentication is included in this app, by which you can register new user
and login to get a token that will be used in some API calls (will be explained in details further)
<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python]][Python-url]
* [![Django][Django]][Django-url]
* [![GrapQL][GraphQL]][GraphQL-url]
* [![JWT][JWT]][JWT-url]
* [![sqlite][sqlite]][sqlite-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started


### Prerequisites

* Python <= 3.10.6
* Pip <= 22.0.2
* Python virtual environment

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/elZomor/student-graphql && cd student-graphql
   ```
2. Create virtual environment
   ```sh
   python3 -m venv venv
   ```
3. Activate virtual environment
   ```sh
   source venv/bin/activate
   ```
4. Install requirements
   ```sh
   pip install -r requirements.txt
   ```
5. Migrate models
   ```sh
   python manage.py migrate
   ```
6. Run server
   ```sh
   python manage.py runserver 0.0.0.0:8002
   ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

We have one endpoint
[http://localhost:8002/graphql/](http://localhost:8002/graphql/)  
Through the previous link, you can find the documentation as per the GraphQL
  
Also, through the [Admin Panel](http://localhost:8002/admin) you can see the models
  
To create a superuser
```sh
python manage.py createsuperuser
```
  
Note that the following mutation is requiring superuser token authentication
"deleteStudent"
  
#### Token  
Pass the access token in header as following:  
```json
{
   "Authorization": "JWT {{TOKEN}}"
}
```
#### Uploading images using postman
* Creating student with picture
* Choose form-data in body
* Choose bulk-edit and put the following  
```
operations:{"query": "mutation($picture: Upload!){createStudent(name: \"Magdy\", age: 20, grade: GRADE_THREE, picture: $picture){success}}","variables": {"picture": null}}
map:{ "0": ["variables.picture"]}
```
* Choose Key-Value edit and put value for key "0" as file and upload picture of student


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Mohamed Elzomor - mohamed.ali.elzomor@gmail.com

Project Link: [https://github.com/elZomor/student-graphql](https://github.com/elZomor/student-graphql)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/mohamed-elzomor
[Django]: https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green
[Django-url]: https://docs.djangoproject.com/en/3.2/
[GraphQL]: https://img.shields.io/badge/GraphQl-E10098?style=for-the-badge&logo=graphql&logoColor=white
[GraphQL-url]: https://graphql.org/
[Python]: https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue
[Python-url]: https://docs.python.org/3/
[sqlite]: https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white
[sqlite-url]: https://www.sqlite.org/index.html
[JWT]: https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=JSON%20web%20tokens&logoColor=white
[JWT-url]: https://jwt.io/