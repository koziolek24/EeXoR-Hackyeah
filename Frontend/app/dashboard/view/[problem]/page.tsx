

export default function Page({ params }: { params: { problem: string } }) {

    return <h1>{params.problem}</h1>
}