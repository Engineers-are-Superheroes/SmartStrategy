import React from "react";
import { LoginContainer, LoginForm, Title, LoginButton, InputBox, LoginFormContainer } from './SignupElements';

const Signup = () => {
    return (
        <LoginContainer>
            <LoginForm>
                <Title>
                    Signup
                </Title>
                <LoginFormContainer>
                    <InputBox type="email" placeholder="Email"/>
                    <InputBox placeholder="Username"/>
                    <InputBox type="password" placeholder="Password" />
                    <InputBox type="password" placeholder="Confirm Password"/>
                    
                    <LoginButton>
                        Signup
                    </LoginButton>
                </LoginFormContainer>
            </LoginForm>
        </LoginContainer>
    )
}

export default Signup;