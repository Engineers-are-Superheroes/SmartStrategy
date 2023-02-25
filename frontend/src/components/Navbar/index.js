import React, { useState } from "react";
import styles from "./styles.module.scss";

function Navbar() {
    //const { t } = useTranslation();
    const [isNavOpen, setIsNavOpen] = useState(false);
    const [isLangOpen, setIsLangOpen] = useState(false);
    //const location = useLocation();

    return (
        <>
            <header className={styles.header}>
                <h1>Test</h1>
            </header>
            {/* <div onClick={() => setIsNavOpen(false)}>
                {isNavOpen && <MobileNavbar />}
            </div> */}
        </>
    )
}

export default Navbar;