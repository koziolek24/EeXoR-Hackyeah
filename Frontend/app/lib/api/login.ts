import { NextResponse } from "next/server";
import { sessionSettings } from "@/app/lib/sessionSettings";


export async function login(path: string, login: string) {
    const apiData = new FormData();
    apiData.set("handle", login);
    const res = await fetch(`${process.env.API_URL}/login/`, {
        method: "POST",
        body: apiData,
    });

    if(!res.ok)
    {
        const response = NextResponse.redirect(new URL("/", path));
        response.cookies.set(sessionSettings.incorrectDataCookieName, "1");
        return response;
    }

    const content = await res.json();
    const userId = content.user_id;

    const response = NextResponse.redirect(new URL("/dashboard", path));
    response.cookies.set(sessionSettings.cookieName, userId.toString());
    return response;
}