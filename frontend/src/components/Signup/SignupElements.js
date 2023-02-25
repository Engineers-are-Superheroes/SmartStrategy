import styled from "styled-components";

export const LoginContainer = styled.div`
    color:white;
    height:90vh;
    overflow: None;
    align-items: center;
    display: flex;
    align-items: center;
    justify-content: center;
    // background-color:red;
`
export const LoginForm = styled.div`

    width: 80vw;
    height: 60vh;
   
    align-items: center;
    justify-content: center;
  
`
export const LoginFormContainer = styled.div`
    margin-top:50px;
    align-items: center;
    justify-content: center;
    color: #24135e;
`

export const Title = styled.div`
    font-size: 2.5rem;
    justify-content: center;
    display:flex;
    color: #24135e;
`

export const LoginButton = styled.button`
    color:white;
    width:20%;
    height:40px;
    font-size: 1.3rem;
    background-color: #24135e;
    border-radius:9px;
    margin: 20px auto;
    display: flex;
    align-items: center;
    justify-content: center;

    &:active{
        color:#24135e;
        background-color:white;
    }
    &:hover{
        cursor:pointer;
    }
    
`

export const InputBox = styled.input`
    width: 40%;
    font-size: 1.3rem;
    height: 30px;
    display: flex;
    margin: 35px auto;
    align-items: center;
    justify-content: center;

`