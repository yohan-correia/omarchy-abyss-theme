from pathlib import Path
import json, zipfile, tomllib
p=Path(__file__).parent
pal=tomllib.loads((p.parent/'colors.toml').read_text())
bg='#06090B'; panel='#0B1219'; raised='#101C26'; border='#253643'; fg='#D8DFE5'; muted='#8296A5'; gold='#C2A46D'; blue='#78A6CC'; sel='#25445B'
c={}
def assign(value, keys):
 for k in keys.split(): c[k]=value
assign(bg,'editor.background terminal.background tab.activeBackground activityBar.background titleBar.inactiveBackground')
assign(panel,'sideBar.background panel.background statusBar.background statusBar.noFolderBackground titleBar.activeBackground editorGroupHeader.tabsBackground tab.inactiveBackground input.background dropdown.background breadcrumb.background')
assign(raised,'editorWidget.background editorHoverWidget.background editorSuggestWidget.background quickInput.background menu.background notifications.background sideBarSectionHeader.background button.secondaryBackground')
assign(fg,'foreground editor.foreground terminal.foreground sideBar.foreground input.foreground dropdown.foreground menu.foreground notifications.foreground editorWidget.foreground editorSuggestWidget.foreground quickInput.foreground statusBar.foreground tab.activeForeground button.secondaryForeground')
assign(muted,'descriptionForeground disabledForeground tab.inactiveForeground tab.unfocusedActiveForeground activityBar.inactiveForeground titleBar.inactiveForeground input.placeholderForeground editorLineNumber.foreground')
assign(border,'sideBar.border panel.border editorGroup.border editorWidget.border editorHoverWidget.border input.border dropdown.border menu.border notifications.border titleBar.border statusBar.border tab.border editorIndentGuide.background1 editorRuler.foreground')
assign(gold,'focusBorder tab.activeBorderTop tab.unfocusedActiveBorderTop tab.activeModifiedBorder panelTitle.activeBorder activityBar.activeBorder activityBar.foreground editorCursor.foreground terminalCursor.foreground editorLineNumber.activeForeground progressBar.background button.background badge.background activityBarBadge.background list.highlightForeground')
assign(bg,'button.foreground badge.foreground activityBarBadge.foreground terminalCursor.background')
assign('#D8BB82','button.hoverBackground')
assign(sel,'editor.selectionBackground terminal.selectionBackground list.activeSelectionBackground list.inactiveSelectionBackground editorSuggestWidget.selectedBackground quickInputList.focusBackground')
assign(fg,'list.activeSelectionForeground list.inactiveSelectionForeground quickInputList.focusForeground editorSuggestWidget.selectedForeground')
assign('#172A39','list.hoverBackground toolbar.hoverBackground tab.hoverBackground button.secondaryHoverBackground')
assign('#C2A46D80','list.focusOutline')
assign('#162B3B','editor.inactiveSelectionBackground')
assign('#0D1720','editor.lineHighlightBackground')
assign('#00000000','editor.lineHighlightBorder tab.activeBorder')
assign('#365B75','editorIndentGuide.activeBackground1')
assign('#C2A46D40','editor.findMatchBackground')
assign(gold,'editor.findMatchBorder')
assign('#25445B80','editor.findMatchHighlightBackground editor.wordHighlightBackground editor.wordHighlightStrongBackground')
assign(blue,'textLink.foreground textLink.activeForeground')
assign('#101C26','textCodeBlock.background textBlockQuote.background')
assign(gold,'textBlockQuote.border')
assign('#25364380','scrollbarSlider.background')
assign('#45617899','scrollbarSlider.hoverBackground scrollbarSlider.activeBackground')
assign('#D7837D','errorForeground editorError.foreground terminal.ansiRed gitDecoration.deletedResourceForeground')
assign('#C2A46D','editorWarning.foreground')
assign(blue,'editorInfo.foreground gitDecoration.modifiedResourceForeground')
assign('#91B79E','gitDecoration.addedResourceForeground')
assign('#102B20','diffEditor.insertedLineBackground')
assign('#341B20','diffEditor.removedLineBackground')
assign('#25445B','statusBar.debuggingBackground statusBarItem.remoteBackground')
assign(fg,'statusBar.debuggingForeground statusBarItem.remoteForeground')
for key,pkey in zip(['Black','Red','Green','Yellow','Blue','Magenta','Cyan','White','BrightBlack','BrightRed','BrightGreen','BrightYellow','BrightBlue','BrightMagenta','BrightCyan','BrightWhite'],['background','red','green','yellow','blue','magenta','cyan','foreground','muted','bright_red','bright_green','bright_yellow','bright_blue','bright_magenta','bright_cyan','bright_foreground']):
 c['terminal.ansi'+key]=pal[pkey]
rules=[('Comments','comment punctuation.definition.comment',muted,'italic'),('Strings','string',pal['green'],''),('Numbers and constants','constant.numeric constant.language constant.character',pal['orange'],''),('Keywords','keyword storage.type storage.modifier',pal['bright_magenta'],''),('Operators','keyword.operator',pal['bright_blue'],''),('Functions','entity.name.function support.function',blue,''),('Types','entity.name.type entity.name.class support.type support.class',gold,''),('Variables','variable',fg,''),('Parameters','variable.parameter',pal['cyan'],''),('Properties','variable.other.property support.type.property-name entity.other.attribute-name',pal['cyan'],''),('Tags','entity.name.tag',blue,''),('Punctuation','punctuation',muted,''),('Markdown headings','markup.heading entity.name.section',gold,'bold'),('Markdown bold','markup.bold',fg,'bold'),('Markdown italic','markup.italic',fg,'italic'),('Markdown code','markup.inline.raw markup.fenced_code.block',pal['green'],''),('Links','markup.underline.link',blue,''),('Inserted','markup.inserted',pal['green'],''),('Deleted','markup.deleted',pal['red'],''),('Changed','markup.changed',gold,'')]
tokens=[{'name':n,'scope':s.split(),'settings':{'foreground':v,**({'fontStyle':style} if style else {})}} for n,s,v,style in rules]
semantic={'variable':fg,'parameter':pal['cyan'],'property':pal['cyan'],'function':blue,'method':blue,'class':gold,'interface':gold,'enum':gold,'type':gold,'typeParameter':gold,'namespace':blue,'decorator':pal['cyan'],'enumMember':pal['orange'],'variable.readonly':pal['bright_yellow'],'string':pal['green'],'number':pal['orange'],'keyword':pal['bright_magenta'],'operator':pal['bright_blue'],'comment':{'foreground':muted,'italic':True}}
theme={'$schema':'vscode://schemas/color-theme','name':'Abyss','type':'dark','semanticHighlighting':True,'colors':c,'tokenColors':tokens,'semanticTokenColors':semantic}
package={'name':'abyss-theme','displayName':'Abyss','description':'Blue-black depths, cool blue selections and antique gold focus. Matches the Abyss Omarchy theme.','version':'1.0.0','publisher':'yohan','engines':{'vscode':'^1.70.0'},'categories':['Themes'],'contributes':{'themes':[{'id':'Abyss','label':'Abyss','uiTheme':'vs-dark','path':'./themes/abyss-color-theme.json'}]}}
# vscode-theme.json at the theme root replaces the one Omarchy would generate from colors.toml
for path,data in [(p/'package.json',package),(p/'themes/abyss-color-theme.json',theme),(p.parent/'vscode-theme.json',theme)]:path.write_text(json.dumps(data,indent=2)+'\n')
manifest='''<?xml version="1.0" encoding="utf-8"?>
<PackageManifest Version="2.0.0" xmlns="http://schemas.microsoft.com/developer/vsx-schema/2011"><Metadata><Identity Language="en-US" Id="abyss-theme" Version="1.0.0" Publisher="yohan"/><DisplayName>Abyss</DisplayName><Description xml:space="preserve">Abyss color theme</Description><Tags>theme,dark</Tags><Categories>Themes</Categories><GalleryFlags>Public</GalleryFlags><Properties><Property Id="Microsoft.VisualStudio.Code.Engine" Value="^1.70.0"/><Property Id="Microsoft.VisualStudio.Code.ExtensionDependencies" Value=""/><Property Id="Microsoft.VisualStudio.Code.ExtensionPack" Value=""/><Property Id="Microsoft.VisualStudio.Code.LocalizedLanguages" Value=""/></Properties></Metadata><Installation><InstallationTarget Id="Microsoft.VisualStudio.Code"/></Installation><Dependencies/><Assets><Asset Type="Microsoft.VisualStudio.Code.Manifest" Path="extension/package.json" Addressable="true"/></Assets></PackageManifest>'''
with zipfile.ZipFile(p/'abyss-theme-1.0.0.vsix','w',zipfile.ZIP_DEFLATED) as z:
 z.writestr('extension.vsixmanifest',manifest)
 z.writestr('[Content_Types].xml','<?xml version="1.0"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="json" ContentType="application/json"/><Default Extension="vsixmanifest" ContentType="text/xml"/></Types>')
 for f in [p/'package.json',p/'themes/abyss-color-theme.json']:z.write(f,'extension/'+str(f.relative_to(p)))
print(f'Built VSIX: {len(c)} UI colors, {len(tokens)} syntax rules, {len(semantic)} semantic rules.')
