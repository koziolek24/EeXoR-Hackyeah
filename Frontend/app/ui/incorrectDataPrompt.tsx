"use client"


import { getCookie, deleteCookie } from 'cookies-next';
import { sessionSettings } from "@/app/lib/sessionSettings";
import { useEffect, useState } from "react";


export default function IncorrectDataPrompt() {

    const [content, setContent] = useState("");

    useEffect(() => {
        const value = getCookie(sessionSettings.incorrectDataCookieName);
        if (value != null) {
            setContent(value);
            deleteCookie(sessionSettings.incorrectDataCookieName);
        }
    }, []);
    return <p className="text-danger mb-3">{content}</p>;
}