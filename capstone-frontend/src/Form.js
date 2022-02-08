import * as React from 'react';
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import Grid from '@mui/material/Grid';
import { styled } from '@mui/material/styles';
import './Form.css';
import ButtonBase from '@mui/material/ButtonBase';

const Item = styled(Paper)(({ theme }) => ({
    ...theme.typography.body2,
    padding: theme.spacing(1),
    textAlign: 'center',
    color: theme.palette.text.secondary,
  }));

function SimplePaper() {
    return (
        <Paper sx={{ p: 2, margin: 'auto', maxWidth: 500, flexGrow: 1 }}>
        <Grid container spacing={2}>
          {/* <Grid item>
            <ButtonBase sx={{ width: 128, height: 128 }}>
                Test
            </ButtonBase>
          </Grid> */}
          <Grid item xs={2} sm container >
            <Item>This is Item</Item>
          </Grid>
          <Grid item xs={12} sm container >
            <Item>This is Item</Item>
          </Grid>
        </Grid>
      </Paper>
        
    )
}

export default SimplePaper