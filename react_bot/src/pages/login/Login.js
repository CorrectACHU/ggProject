import style from './style.css'
import {useHistory} from "react-router-dom";
import {useContext, useState} from "react";

const Login = () => {
    const [emailValue, setEmailValue] = useState('')
    const [passwordValue, setPasswordValue] = useState('')
    const [isLoading, setLoading] = useState(false)
    const [data, setData] = useState([])
    const contextData = useContext()
    const history = useHistory()
    const handleClick = async (e) => {
        e.preventDefault()
        setLoading(!isLoading)
        const stringifyData = JSON.stringify({
            email: emailValue,
            password: passwordValue,

        })
        await fetch('http://127.0.0.1:5000', {
            method: "POST",
            body: JSON.stringify(stringifyData),
            headers: {
                "Content-Type": "application/json"
            }
        })
            .then(res => {
                console.log(res, 'RAW_RES')
                return res.json()
            })
            .then(resp => {
                console.log(JSON.parse(resp), 'JSON_PARSE_RES')
                setData(JSON.parse(resp))
                history.push('/set-filters')
            })
            .catch(e => {
                alert('Произошла какая-от ху*та')
                console.log('Вот описание ху*ты:' ,e)
            })
            .finally(() => {
                setLoading(false)
            })
    }
    return (
        <div className="wrapper">
            {isLoading ? (<div className='loader-wrapper'>
                <div className="lds_default">
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
            </div>
                <span className='loader-text'>Wait a minute please. Bot are preparing the data.</span>
            </div>) : <form className={style.form_registration}>
                <input onChange={(e) => setEmailValue(e.target.value)} type="email" name="email"
                       className="email-input"/>
                <input onChange={(e) => setPasswordValue(e.target.value)} type="password" name="password"
                       className="pass-input"/>
                <button onClick={handleClick} className="submit-btn">
                    login
                </button>
            </form>}
        </div>
    );
};

export default Login;