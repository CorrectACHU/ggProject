import style from './style.css';
import {Link} from "react-router-dom";

const Start = () => {
    return (
        <div>
            <div>
                <Link to="/login" className="start-link">
                    start
                </Link>
            </div>
        </div>
    );
};

export default Start;