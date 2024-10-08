"use client"


import { getCookie, deleteCookie } from 'cookies-next';
import { sessionSettings } from "@/app/lib/sessionSettings";
import { useEffect, useState } from "react";


export default function IncorrectDataPrompt({message}: {message: string}) {

    const [content, setContent] = useState("");

    useEffect(() => {
        if (getCookie(sessionSettings.incorrectDataCookieName) == "1") {
            deleteCookie(sessionSettings.incorrectDataCookieName);
            setContent(message);
        }
    }, [message]);
    return <p className="text-danger mb-3">{content}</p>;
}