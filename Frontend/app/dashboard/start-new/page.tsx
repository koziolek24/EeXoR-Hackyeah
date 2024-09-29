


export default function Page() {
    return <form>
        <div>
            <input type="radio" name="select-method" id="bytag" value="bytag"/>
            <label htmlFor="bytag">By tag</label>
        </div>

        <div>
            <input type="radio" name="select-method" id="rand" value="rand"/>
            <label htmlFor="rand">Random</label>
        </div>

        <div>
            <input type="radio" name="select-method" id="prand" value="prand"/>
            <label htmlFor="prand">Build your skills</label>
        </div>
        <input type="submit" value="Start new problem!"/>
    </form>;
}