import {sessionSettings} from "@/app/lib/sessionSettings";


export type RegisterResult = {
    status: boolean;
    cookieName: string;
    cookieValue: string;
}

export async function register(login: string) : Promise<RegisterResult> {
    const apiData = new FormData();
    apiData.set("handle", login);
    apiData.set("rank", "100");
    apiData.set("rating", "100")
    const res = await fetch(`${process.env.API_URL}/register/`, {
        method: "POST",
        body: apiData,
    });

    if(!res.ok)
    {
        return {
            status: false,
            cookieName: sessionSettings.incorrectDataCookieName,
            cookieValue: "Sorry! Login is already in use!",
        };
    }

    return {
        status: true,
        cookieName: "",
        cookieValue: "",
    }
}