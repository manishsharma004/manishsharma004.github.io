import styled from "styled-components";

const LinksContainer = styled.ol`
    padding: 0;
    margin: 0;
`;
const LI = styled.li``;

export default function Home() {
    return (
        <LinksContainer>
            <LI>
                <a href="pro.jsonlint.com/index.html">JSON</a>
            </LI>
            <LI>
                <a href="mobile-preview/index.html">Mobile Preview</a>
            </LI>
        </LinksContainer>
    );
}
