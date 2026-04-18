-- Generated Script
local fields = { "word", "longerwor", "other" }
function onLoad()
    self.UI.setXml(generateCardXml())
end

-- Helper to create a cell with a border and text
function createTableCell(xml, text, widthWeight, heightWeight, borderColor, borderWidth)
    -- Start Panel acting as a 'cell'
    xml = xml .. '<Panel color="#00000001" ' -- Nearly transparent bg
    if widthWeight then xml = xml .. 'width="' .. widthWeight .. '" ' end
    if heightWeight then xml = xml .. 'height="' .. heightWeight .. '" ' end
    xml = xml .. '>'

    -- Cell Border (Inner)
    xml = xml .. '<Outline color="' .. borderColor .. '" size="' .. borderWidth .. ' ' .. borderWidth .. '" />'

    -- Cell Text
    xml = xml ..
    '<Text text="' .. text .. '" fontSize="14" color="' .. borderColor ..
    '" alignment="MiddleCenter" padding="0 0 0 0" />'
    xml = xml .. '</Panel>'
    return xml
end

function generateCardXml()
    local num = #fields
    local width = 180
    local height = 20
    local borderColor = "#FF0000"
    local borderWidth = "2"

    -- Main Container Panel (Outer border is handled by Layouts usually)
    local xml = '<Panel id="DebugBox" width="' .. width .. '" height="' .. height .. '" '
    xml = xml .. 'scale="1 1 1" position="0 70 -40" '
    xml = xml .. 'rotation="0 0 180" color="#00000000">' -- Transprent container

    -- 4. Dynamic Layout Decision
    if num == 3 then
        -- T-Shape (2 on top, 1 centered below)
        -- We use a Vertical Layout to split top/bottom
        xml = xml .. '<VerticalLayout spacing="0" padding="0 0 0 0">'

        -- Top Row (using HorizontalLayout)
        xml = xml .. '<HorizontalLayout spacing="0" height="10" padding="0 0 0 0">'
        xml = createTableCell(xml, fields[1], "90", nil, borderColor, borderWidth)         -- Width 90 (half)
        xml = createTableCell(xml, fields[2], "90", nil, borderColor, borderWidth)         -- Width 90 (half)
        xml = xml .. '</HorizontalLayout>'

        -- Bottom Row (Single centered cell)
        xml = xml .. '<HorizontalLayout spacing="0" height="10" padding="0 0 0 0">'
        xml = createTableCell(xml, fields[3], "180", nil, borderColor, borderWidth)         -- Full width
        xml = xml .. '</HorizontalLayout>'

        xml = xml .. '</VerticalLayout>'
    elseif num == 4 then
        -- 2x2 Grid
        xml = xml .. '<VerticalLayout spacing="0" padding="0 0 0 0">'

        -- Top Row (using HorizontalLayout)
        xml = xml .. '<HorizontalLayout spacing="0" height="10" padding="0 0 0 0">'
        xml = createTableCell(xml, fields[1], "90", nil, borderColor, borderWidth)
        xml = createTableCell(xml, fields[2], "90", nil, borderColor, borderWidth)
        xml = xml .. '</HorizontalLayout>'

        -- Bottom Row
        xml = xml .. '<HorizontalLayout spacing="0" height="10" padding="0 0 0 0">'
        xml = createTableCell(xml, fields[3], "90", nil, borderColor, borderWidth)
        xml = createTableCell(xml, fields[4], "90", nil, borderColor, borderWidth)
        xml = xml .. '</HorizontalLayout>'

        xml = xml .. '</VerticalLayout>'
    else
        -- Fallback: Simple Horizontal Row (for 1, 2, or >4 words)
        xml = xml .. '<HorizontalLayout spacing="0" height="20" padding="0 0 0 0">'

        -- Outline goes on the container here
        xml = xml .. '<Outline color="' .. borderColor .. '" size="' .. borderWidth .. ' ' .. borderWidth .. '" />'

        local spacing = width / (num + 1)
        for i, word in ipairs(fields) do
            local xOffset = -(width / 2) + (spacing * i)
            xml = xml ..
            '<Text text="' ..
            word ..
            '" offsetXY="' .. xOffset .. ' 0" fontSize="14" color="' .. borderColor .. '" alignment="MiddleCenter" />'
        end
        xml = xml .. '</HorizontalLayout>'
    end

    xml = xml .. '</Panel>'
    return xml
end
