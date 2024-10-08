"use client"


import { getCookie, deleteCookie } from 'cookies-next';
import { sessionSettings } from "@/app/lib/sessionSettings";
import { useEffect, useState } from "react";


export default function IncorrectDataPrompt() {

    const [content, setContent] = useState("");

    useEffect(() => {
        if (getCookie(sessionSettings.incorrectDataCookieName) == "1") {
            deleteCookie(sessionSettings.incorrectDataCookieName);
            setContent("Please enter valid login!");
        }
    }, []);
    return <p className="text-danger mb-3">{content}</p>;
}