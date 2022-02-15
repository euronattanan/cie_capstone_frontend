import * as React from 'react';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import './NewForm.css'
import MenuItem from '@mui/material/MenuItem';

const vaccine_num = [
    {
        value: 1,
        label: '1'
    },
    {
        value: 2,
        label: '2'
    },
    {
        value: 3,
        label: '3'
    },
    {
        value: 4,
        label: '4'
    },
    {
        value: 5,
        label: '5'
    }
]
const vaccine_type = [
    {
        value: "moderna",
        label: "Moderna"
    },
    {
        value: "pfizer",
        label: "Pfizer"
    },
    {
        value: "sinovac",
        label: "Sinovac"
    },
    {
        value: "sinopharm",
        label: "Sinopharm"
    },
    {
        value: "astrazeneca",
        label: "AstraZeneca"
    }
]

// const vacine_type = [
//     {
//         value:"moderna",
//         label:"Moderna"
//     }
// ]


// useState for vaccine type
// const [vaccineType, setVaccineType] = React.useState("");

function NewForm(){
    // useState for vaccine number
    const [vaccine, setVaccine] = React.useState(0);
    
    // useState for vaccine type
    const [vaccineType, setVaccineType] = React.useState([]);
    const [info, setInfo] = React.useState({
        fname: "",
        lname: "",
        contact: null,
        vaccine: 0,
        vaccineType: [],
    })

    const handleVaccineChange = (event) => {
        event.preventDefault();

        setVaccine(event.target.value);
    }
    
    const handleVaccineTypeChange = (event) => {
        event.preventDefault();
        setVaccineType(arr=>[...arr,event.target.value])
        
    }

    const handleOnSubmit = (e) => {
        e.preventDefault();

        console.log(info)
    }

    function handleChange(evt) {
        const value = evt.target.value;
        setInfo({
          ...info,
          [evt.target.name]: value
        });
      }

    
    return(
        <div className="card mt-4" style={{width: '29rem'}}>

        
        <Box
        component="form" 
        sx={{
          '& .MuiTextField-root': { m: 1 },
        }}
        className="form-container"
        >
            <h1 className="text-center pt-5">No(Co)vid-19</h1>
            <h3 className="text-center">Form for Vaccine checking</h3>
            <div>
                <TextField
                    required
                    id="standard-password-input"
                    label="Firstname"
                    type="text"
                    name="fname"
                    variant="standard"
                    value={info.fname}
                    onChange={handleChange}
                />
                <TextField
                    required
                    id="standard-password-input"
                    label="Lastname"
                    type="lastname"
                    name="lname"
                    variant="standard"
                    value = {info.lname}
                    onChange = {handleChange}
                />
            </div>
            <div className='contact'>
                <TextField
                    required
                    id="standard-password-input"
                    label="Contact"
                    type="contact"
                    name="contact"
                    variant="standard"
                    value={info.contact}
                    onChange = {handleChange}
                />
            </div> 
            <div className="vac_num">
                <TextField
                    id="select-vaccine-num"
                    select
                    label="Select number of vaccine"
                    value={vaccine}
                    onChange={handleVaccineChange}
                    helperText="Please select number of vaccine you received"
                    variant="standard"
                >
                    {vaccine_num.map((option) => (
                        <MenuItem key={option.value} value={option.value}>
                            {option.label}
                        </MenuItem>
                    ))}
                </TextField>
                Number of Vaccine: {vaccine}
            </div>
            <div className='vaccineType'>
                {Array(vaccine).fill().map((_,i) => (
                    <TextField
                        id="select-vaccine-type"
                        select
                        label="Select type of vaccine #"
                        value={vaccineType[i]}
                        onChange={handleVaccineTypeChange}
                        helperText="Please select type of vaccine you received"
                        variant="standard"
                    >
                        {vaccine_type.map((option) => (
                            <MenuItem key={option.value} value={option.value}>
                                {option.label}
                            </MenuItem>
                        ))}
                    </TextField> 
                ))}      
            </div>
            <div className="text-center pb-3">
                <button className='btn btn-success me-4' onClick={handleOnSubmit}>Submit</button>
                <button className='btn btn-secondary'>Cancel</button>
            </div>
        </Box>
            </div>
    );
}


export default NewForm