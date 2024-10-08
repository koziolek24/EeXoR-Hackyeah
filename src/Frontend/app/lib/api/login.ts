import {sessionSettings} from "@/app/lib/sessionSettings";


export type LoginResult = {
    status: boolean;
    cookieName: string;
    cookieValue: string;
}

export async function login(login: string) : Promise<LoginResult> {
    const apiData = new FormData();
    apiData.set("handle", login);
    const res = await fetch(`${process.env.API_URL}/login/`, {
        method: "POST",
        body: apiData,
    });

    if(!res.ok)
    {
        return {
            status: false,
            cookieName: sessionSettings.incorrectDataCookieName,
            cookieValue: "Please enter valid login!",
        };
    }

    const content = await res.json();
    const userId = content.user_id;

    return {
        status: true,
        cookieName: sessionSettings.cookieName,
        cookieValue: userId.toString(),
    };
}