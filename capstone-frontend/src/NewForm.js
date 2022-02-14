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
    const [vaccineType, setVaccineType] = React.useState("");

    const handleVaccineChange = (event) => {
        event.preventDefault();

        setVaccine(event.target.value);
    }
    
    const handleVaccineTypeChange = (event) => {
        event.preventDefault();
        setVaccineType(event.target.value)
    }

    return(
        <Box
        component="form" 
        sx={{
          '& .MuiTextField-root': { m: 1, width: '25ch' },
        }}
        className="form-container"
        >
            <h1>No(Co)vid-19</h1>
            <h3>Form for Vaccine checking</h3>
            <div>
                <TextField
                    required
                    id="standard-password-input"
                    label="Firstname"
                    type="firstname"
                    variant="standard"
                />
                <TextField
                    required
                    id="standard-password-input"
                    label="Lastname"
                    type="lastname"
                    variant="standard"
                />
            </div>
            <div className='contact'>
                <TextField
                    required
                    id="standard-password-input"
                    label="Contact"
                    type="contact"
                    variant="standard"
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
                        // value={vaccineType}
                        // onChange={handleVaccineTypeChange}
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
                Type of Vaccine: {vaccineType} 
            </div>
            <button className='buttonSubmit'>Submit</button>
            <button className='buttonCancel'>Cancel</button>
        </Box>
    );
}


export default NewForm