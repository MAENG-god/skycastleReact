import React from "react";
import axios from 'axios';

class Students extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            students:[],
        };
    }

    async componentDidMount(){
        axios.get("http://localhost:8000/management/students/")
            .then((response) => {
                this.setState({students : response.data})
            })
            .catch((response) => {
                console.log(response)
            }
            )
    }
    render(){
        return(
            <div>
                {this.state.students.map((student => (
                    <div key={student.id}>
                        <div>{student.studentName}</div>
                    </div>
                )))}
            </div>
        )
    }
}

export default Students