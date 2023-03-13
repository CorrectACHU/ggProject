import style from './style.css'
import {useHistory} from "react-router-dom";
import {useState} from "react";

const Login = () => {
    const [emailValue, setEmailValue] = useState('')
    const [passwordValue, setPasswordValue] = useState('')
    const [linkValue, setLinkValue] = useState('')
    const [messageValue, setMessageValue] = useState('')
    const [isLoading, setLoading] = useState(false)
    const history = useHistory()
    const handleClick = async (e) => {
        e.preventDefault()
        setLoading(!isLoading)
        const stringifyData = JSON.stringify({
            email: emailValue,
            password: passwordValue,
            link: linkValue,
            message: messageValue,

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
                <div className="form-item">
                    <label>
                        Email
                    </label>
                    <input onChange={(e) => setEmailValue(e.target.value)} type="email" name="email"
                           className="email-input"/>
                </div>
                <div className="form-item">
                    <label>
                        Password
                    </label>
                    <input onChange={(e) => setPasswordValue(e.target.value)} type="password" name="password"
                           className="pass-input"/>
                </div>
                <div className="form-item">
                    <label>
                        Link
                    </label>
                    <input onChange={(e) => setLinkValue(e.target.value)} type="text" name="link"
                           className="link-input"/>
                </div>
                <div className="form-item">
                    <label>
                        Message
                    </label>
                    <textarea maxLength={140} onChange={(e) => setMessageValue(e.target.value)} name="message"
                              className="message-input"/>
                </div>
                <button onClick={handleClick} className="submit-btn">
                    Login
                </button>
            </form>}
        </div>
    );
};

export default Login;